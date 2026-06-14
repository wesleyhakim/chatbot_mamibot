import streamlit as st

def run():
    st.title("Selamat Datang di Resto Mam Sedap")

    st.write("#### Rasakan cita rasa masakan nusantara yang sedap. Mam yang sedap-sedap aja!")

    st.success("👉 Buka halaman Chatbot untuk mulai bertanya tentang menu, promo, dan informasi restoran.")
    
    with st.expander("📖 Project description:"):
        st.markdown("""
        Mam Sedap adalah restoran fiktif dengan chatbot bernama MamiBot. MamiBot merupakan chatbot berbasis Large Language Model (LLM) yang ditugaskan untuk memberikan informasi kepada pelanggan mengenai informasi umum restoran, menu, serta promo atau diskon yang ditawarkan restoran. 
        MamiBot menggunakan Retrieval-Augmented Generation untuk mengoptimalkan output agar jawaban chatbot akurat. Data yang digunakan berupa teks PDF berisi informasi umum restoran, menu, serta promo yang tersedia. Dokumen tersebut diproses menjadi vektor menggunakan model embedding Gemini dalam representasi vektor berdimensi 768,
        kemudian disimpan dan diindeks menggunakan FAISS. Ketika user bertanya, teks pertanyaan tersebut juga diubah menjadi vektor menggunakan model embedding yang sama dan dilakukan similarity search dengan database vektor dari teks PDF untuk mencari informasi yang paling relevan, 
        dan LLM akan memproses informasi tersebut dan menjawab pertanyaan dari user. Selain memanfaatkan RAG, MamiBot juga menggunakan riwayat percakapan untuk memahami konteks pertanyaan lanjutan agar percakapan
        terasa natural dan kontekstual. Model LLM yang digunakan adalah Gemini 2.5 Flash dengan Google AI Studio API Key. Maka dari itu, API Key yang didukung pada aplikasi ini hanyalah API key Google AI Studio.
        """)
        st.caption("* Dokumen PDF yang digunakan sebagai data RAG ada pada halaman PDF Data")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("LLM", "🤖 Gemini 2.5 Flash")

    with col2:
        st.metric("Embedding Vektor", "🔢 768 Dimensi")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Vector DB", "🔍 FAISS")
    
    with col2:
        st.metric("Method", "📚 RAG")
    
    st.markdown("---")
    
    st.markdown("""
    ## 🌟 Creator
    Wesley Hakim   
    LinkedIn: [🔗 Connect](https://www.linkedin.com/in/wesley-hakim/)   
    Github: [✅ Follow](https://github.com/wesleyhakim)
    """)


    st.markdown("---")
    st.caption("© 2026 MamiBot | Wesley Hakim")

if __name__ == "__main__":
    run()