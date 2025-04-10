import os

import chromadb
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    CHROMA_PATH = "data/chroma_lang"
    chroma_collection_name = "news_articles"
    DISTANCE_THRESHOLD = 0.5
    TOP_K = 5
    MAX_TOKENS = 1000
    TEMPERATURE = 0.7
    MODEL_NAME = "gpt-3.5-turbo"
    embedding_model = "text-embedding-ada-002"
    openai_client = OpenAI(api_key=OPENAI_API_KEY)
    embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = chroma_client.get_or_create_collection(chroma_collection_name)
