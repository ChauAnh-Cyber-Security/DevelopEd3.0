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
#---------------------------------------------------------------------------

def uploadNote():
    print("\nWorking on it!")

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
    Chroma.from_documents(documents=doc, embedding=embeddings, persist_directory=persist_directory)

    print("Knowledge updated!")

    

