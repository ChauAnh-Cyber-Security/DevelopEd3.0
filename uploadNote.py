#---------------------------------------------------------------------------
# Summary: This function specifically translate files in gemini_folder 
#          from natural languages to embedded vectors
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
# SETUP
from getLlmRetriever import*
from embedGetter import*

import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
#---------------------------------------------------------------------------

def uploadNote():
    print("\nWorking on it! Make sure all your needed files are in a folder called 'gemini_folder'")

    # Set the directory for the permanent directory
    persist_directory = os.path.join(os.getcwd(), "permanent_library")

    # Check if the directory exists; if not, create it
    if not os.path.exists(persist_directory):
        os.makedirs(persist_directory)

    #initialize an empty document for all file paths
    documents = []
    gemini_folder = os.path.join(os.getcwd(), "gemini_folder")

    # Load PDF files from 'gemini_folder'
    for file in os.listdir(gemini_folder):
        if file.endswith(".pdf"):
            pdf_path = './gemini_folder/' + file
            loader = PyPDFLoader(pdf_path)
            documents.extend(loader.load())

    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=1000)
    doc = text_splitter.split_documents(documents)

    #get embedding
    embeddings = embedGetter()

    #save files to permanent folder
    vectordb = Chroma.from_documents(documents=doc, embedding=embeddings, persist_directory=persist_directory)

    # Create retriever and LLM
    retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 1})
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3, google_api_key=os.getenv('GOOGLEAI_API_KEY'))

    print("Knowledge updated!")

    return llm, retriever

    

