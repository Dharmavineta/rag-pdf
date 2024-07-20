import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser


def main():
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")
    st.header("Chat with multiple PDFs :books:")
    st.text_input("Ask a question about your document")
    
    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your PDFs here and click on process")
        st.button("Process")

if __name__ == '__main__':
    main()
