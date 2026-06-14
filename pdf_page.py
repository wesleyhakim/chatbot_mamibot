import streamlit as st
import base64
from pathlib import Path
from streamlit_pdf_viewer import pdf_viewer

def run():

    BASE_DIR = Path(__file__).parent
    PDF_DIR = BASE_DIR / "Data_Mam_Sedap.pdf"

    st.title("PDF Data")

    st.write("#### Berikut adalah PDF berisi data yang digunakan untuk RAG dari chatbot.")

    st.success("👉 Buka halaman Chatbot untuk mulai bertanya tentang menu, promo, dan informasi restoran.")
    
    with open(PDF_DIR, "rb") as f:
        pdf_bytes = f.read()

        st.download_button(
            "📄 Download PDF",
            pdf_bytes,
            file_name="Data_Mam_Sedap.pdf",
            mime="application/pdf"
        )

    pdf_viewer(PDF_DIR, width=800, height=900)
    
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