import streamlit as st
def main():
    st.set_page_config(page_title="Chat with multiple PDF's", page_icon=":books:")
    st.header("Chat with multiple PDF's :books:")
    st.text_input("Ask a question about your document")
    

    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your PDF's here and click on process")


    


if __name__ == '__main__':
    main()
