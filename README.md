# MamiBot Customer Service Bot for Restaurant

## Repository Outline
```
    chatbot_mamibot
    |
    ├── faiss_index/
    │   ├── index.faiss
    │   └── index.pkl
    ├── Data Mam Sedap.docx
    ├── Data_Mam_Sedap.pdf
    ├── README.md
    ├── chatbot_page.py
    ├── chatbot_test.ipynb
    ├── home_page.py
    ├── pdf_page.py
    └── streamlit_app.py

```
- **chatbot_mamibot**  
    This GitHub repository.

- **faiss_index**  
    Folder that consists of vector database files from PDF file embedding.

- **Data Mam Sedap.docx**  
    docx file to create the pdf data.

- **Data_Mam_Sedap.pdf**  
    The PDF file that is embedded and used for ChatBot to response.

- **README.md**  
    Documentation file that provides an overview and description of this repository.

- **chatbot_page.py**  
    Streamlit code for Chatbot page at huggingface deployment.

- **chatbot_test.ipynb**  
    Notebook to create the vector database using FAISS and test the LLM RAG response based on the vector database.

- **home_page.py**  
    Streamlit code for Home page at huggingface deployment.
  
- **pdf_page.py**  
    Streamlit code for PDF page at huggingface deployment.

- **streamlit_app.py**  
    Streamlit code for main app and navigation bar.

## Problem Background
In this digital era, customers can reach customer services easier using their smartphone or other devices. This make companies require a customer service to response to customer questions and engage with customer. But even having a human customer service can still have inefficiencies as customer service availability and count are limited than the customers demand. Having a chatbot is a good solution for this as chatbot will always be available and can response to multiple customer at once. Though it is important that the chatbot still feel interactive and give an accurate response based on the customer questions. In this example, a fictional restaurant called "Mam Sedap" are used.

## Project Output
The output of this project is a chatbot that can response to a user (customers) questions accurately based on the restaurant's data. The chatbot should be deployed as a web application with a user interface too, allowing accesibility for customers.

## Method
This project utilizes various Large Language Model and Retrieval Augmented Generation to optimize chatbot's response accuracy. Data are stored inside a text PDF which lists restaurant's general information, menu, and discount offers. The PDF document are vectorized using Gemini's embedding model with 768 dimensionality. This vectors are stored and indexed using FAISS. User questions are vectorized using the same embedding model and a similarity search are performed to the PDF vector database to obtain the relevant information for LLM to process and answer the user's question. The chatbot also utilized chat history to understand follow up question contexts and make chat feel more natural and contextual. Gemini 2.5 Flash LLM are used for this project through Google AI Studio API Key. These project only supports Google AI Studio API Key.

## Stacks
This project uses the **Python programming language**. The libraries utilized include **streamlit**, **langchain**, and **FAISS**.

The **web application** is also built using Python and is deployed on the **Hugging Face** platform using **Docker**.



## Reference
- [HuggingFace Web Application Deployment](https://huggingface.co/spaces/wesleyhakim/chatbot_mamsedap)


---
