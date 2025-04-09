import os
import chromadb
from chromadb.config import Settings
from typing import List, Dict

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

chroma_client = chromadb.PersistentClient(path="data/chroma")
chroma_client.delete_collection("news_articles")
collection = chroma_client.get_or_create_collection(name="news_articles")

def get_embedding(text: str) -> List[float]:
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=[text]
    )
    return response.data[0].embedding

def add_to_vector_store(articles: List[Dict[str, str]]) -> None:
    for i, article in enumerate(articles):
        if not article.get("summary"):
            continue
        text_for_embedding = f"Topics: {', '.join(article.get('topics', []))} Title: {article['title']} Summary: {article['summary']} "
        embedding = get_embedding(text_for_embedding)

        collection.add(
            ids=[f"article_{i}"],
            embeddings=[embedding],
            documents=[article["summary"]],
            metadatas=[{
                "url": article["url"],
                "title": article["title"],
                "topics": ", ".join(article.get("topics", []))
            }]
        )
