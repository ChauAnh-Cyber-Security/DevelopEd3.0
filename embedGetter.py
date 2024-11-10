import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def embedGetter():
    # Load embeddings
    load_dotenv()
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.getenv('GOOGLEAI_API_KEY'))

    return embeddings