import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template = """
    Generate a question paper based on the following parameters:
    
    Context:
    {context}

    Parameters:
    - Difficulty level: {difficulty_level}
    - Topic categories: {topic_categories}
    - Maximum marks: {max_marks}
    - Important topics: {important_topics}
    
    Please create a question paper that covers the specified topics, adheres to the difficulty level, and distributes the marks appropriately.

    Generated Question Paper:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

    prompt = PromptTemplate(template=prompt_template, input_variables=[
                            "context", "difficulty_level", "topic_categories", "max_marks", "important_topics"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

def user_input(user_question, difficulty_level, topic_categories, max_marks, important_topics):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    response = chain({
        "input_documents": docs, 
        "question": user_question,
        "difficulty_level": difficulty_level,
        "topic_categories": topic_categories,
        "max_marks": max_marks,
        "important_topics": important_topics
    }, return_only_outputs=True)

    print(response)
    st.write("Generated Question Paper: ", response["output_text"])

def main():
    st.set_page_config("Question Paper Generator")
    st.header("QUESTION PAPER GENERATOR")

    user_question = st.text_input("Provide the context or any specific instruction for generating the question paper")

    difficulty_level = st.selectbox("Select Difficulty Level", ["Easy", "Medium", "Hard"])
    topic_categories = st.text_area("Enter Topic Categories (comma-separated)")
    max_marks = st.number_input("Enter Maximum Marks", min_value=1, max_value=100)
    important_topics = st.text_area("Enter Important Topics to be Covered (comma-separated)")

    if st.button("Generate Question Paper"):
        if user_question and topic_categories and important_topics:
            user_input(user_question, difficulty_level, topic_categories, max_marks, important_topics)
        else:
            st.error("Please provide all necessary inputs.")

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")

if __name__ == "__main__":
    main()
