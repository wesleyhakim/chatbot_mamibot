import streamlit as st
import os
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from pathlib import Path

BASE_DIR = Path(__file__).parent
FAISS_DIR = BASE_DIR / "faiss_index"

@st.cache_resource
def load_vector_store():
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2",
        output_dimensionality=768
    )

    return FAISS.load_local(
        str(FAISS_DIR),
        embeddings,
        allow_dangerous_deserialization=True
    )

st.title("👩‍🍳 MamiBot")
st.write("#### Chatbot informasi Resto Mam Sedap")


if "api_key" not in st.session_state:
    st.session_state["api_key"] = ""

if st.session_state["api_key"] == "":
    st.warning("🔑 Chatbot ini hanya mendukung **API Key dari Google AI Studio (Gemini)**. "
        "API key dari OpenAI, Anthropic, atau provider lain tidak dapat digunakan."
    )
    input_api_key = st.text_input("🔑 API Key:", type="password")
    submit_key = st.button("Submit Key")
    if submit_key:
        st.session_state["api_key"] = input_api_key
    if st.session_state["api_key"] != "":
        st.rerun()
    st.stop()

os.environ["GOOGLE_API_KEY"] = st.session_state["api_key"]

vector_store = load_vector_store()

llm_client = ChatGoogleGenerativeAI(model="gemini-2.5-flash", streaming=True, temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", """
     
Anda adalah bot customer service dan pelayan restoran Mam Sedap dengan nama MamiBot. Selalu menyebut diri anda dengan nama MamiBot. 

Tujuan Anda bukan hanya menjawab pertanyaan, tetapi mengundang pelanggan untuk bertanya lebih dan membuat pelanggan tertarik dengan restoran.

Gunakan bahasa Indonesia yang hangat, ramah, dan mengundang.
Berikan rekomendasi beserta alasan.
Gunakan emoji secukupnya.
Jika pelanggan meminta rekomendasi makanan, jelaskan cita rasa dan kecocokannya.
Akhiri dengan pertanyaan lanjutan yang bersedia menjawab pertanyaan pelanggan.
Gunakan riwayat percakapan secukupnya untuk menentukan maksud pertanyaan pelanggan jika diperlukan.

Jawab pelanggan sesuai dengan bahasa pelanggan.

Peraturan:
- Jangan buat kode apapun
- Jangan menjawab pertanyaan yang tidak berhubungan
- Jangan mengarang informasi yang tidak ada pada context.
- Jika informasi tidak ditemukan pada context, katakan bahwa anda tidak memiliki informasi tersebut dan sarankan untuk langsung menghubungi restoran melalui email atau telepon.
- Jangan sebut diri Anda sebagai Saya atau Aku atau kata lainnya, selalu gunakan nama anda yaitu MamiBot

Gaya Jawaban:
- Prioritaskan menjawab pertanyaan pelanggan secara langsung.
- Sesuaikan panjang jawaban dengan kompleksitas pertanyaan.
- Untuk pertanyaan sederhana, berikan jawaban singkat dan jelas.
- Jangan memberikan informasi yang tidak ditanyakan.
- Jelaskan cita rasa, bahan, atau keunggulan menu hanya jika pelanggan meminta rekomendasi atau detail menu.
- Saat menyebut beberapa menu, gunakan bullet list dan maksimal 3 menu.
- Tetap ramah dan mengundang tanpa bertele-tele.

Context:
{context}

Riwayat Percakapan:
{chat_history}
          
"""),
    ("human", "{question}")
])

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

for chat in st.session_state["chat_history"]:
    if type(chat) is HumanMessage:
        role = "human"
    elif type(chat) is SystemMessage:
        continue
    else:
        role = "ai"
    with st.chat_message(role):
        st.markdown(chat.content)

user_input = st.chat_input("Tanyakan informasi Mam Sedap, menu, atau promo...")

if not user_input:
    st.stop()


st.session_state["chat_history"].append(HumanMessage(user_input))

with st.chat_message("human"):
    st.markdown(st.session_state["chat_history"][-1].content)


history_text = "\n".join(
    [
        f"Pelanggan: {msg.content}"
        if isinstance(msg, HumanMessage)
        else f"Bot: {msg.content}"
        for msg in st.session_state["chat_history"][-5:]
    ]
)

search_query = f"""
Riwayat:
{history_text}

Pertanyaan terbaru:
{user_input}
"""

retrieved_docs = vector_store.similarity_search(search_query, k=4)

docs_content = "\n\n".join(
    doc.page_content
    for doc in retrieved_docs
)

messages = prompt.invoke({
    "question": user_input,
    "context": docs_content,
    "chat_history": history_text
})

with st.chat_message("ai"):
    placeholder = st.empty()

    full_response = ""

    for chunk in llm_client.stream(messages):
        if chunk.content:
            full_response += chunk.content
            placeholder.markdown(full_response)

response = AIMessage(content=full_response)

st.session_state["chat_history"].append(response)
st.rerun()