import streamlit as st

st.set_page_config(
    page_title='Restaurant Chatbot',
    layout='wide'
)

# pages dari app
halaman_home = st.Page("home_page.py", title="Home", icon=":material/home:")
halaman_pdf = st.Page("pdf_page.py", title="PDF Data", icon=":material/edit_document:")
halaman_chatbot = st.Page("chatbot_page.py", title="Chatbot", icon=":material/chat:")

# Buat navigation bar
pg = st.navigation([halaman_home, halaman_pdf, halaman_chatbot], position="top")

# Jalankan page yang dipilih
pg.run()