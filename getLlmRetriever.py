#---------------------------------------------------------------------------
# Summary: This function gets the current LLM and retriever to avoid code redundancy
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
# SETUP
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
#---------------------------------------------------------------------------

def getLlmRetriever():
    # Load embeddings
    load_dotenv()
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.getenv('GOOGLEAI_API_KEY'))
    persist_directory = os.path.join(os.getcwd(), "permanent_library")

    # Load up database from our permanent library
    vectordb = Chroma(embedding_function=embeddings, persist_directory=persist_directory)

    # Create retriever and LLM
    retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 1})
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3, google_api_key=os.getenv('GOOGLEAI_API_KEY'))

    return llm, retriever