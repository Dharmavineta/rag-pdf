import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from PyPDF2 import PdfReader
from langchain_text_splitters import TextSplitter

def get_pdf_text(pdf_docs):
    print("hello")
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+=page.extract_text()
        

    return text
        


def get_text_chunks(raw_text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=100, separators="\n")
    chunks=text_splitter.split_text(raw_text)
    return chunks



def main():
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")
    st.header("Chat with multiple PDFs :books:")
    st.text_input("Ask a question about your document")
    
    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs= st.file_uploader("Upload your PDFs here and click on process", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                raw_text= get_pdf_text(pdf_docs)


                text_chunks= get_text_chunks(raw_text)
                
            

if __name__ == '__main__':
    main()
