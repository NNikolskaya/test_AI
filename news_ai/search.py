import os
from dotenv import load_dotenv
from typing import List
from openai import OpenAI
import chromadb

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
chroma_client = chromadb.PersistentClient(path="data/chroma")
collection = chroma_client.get_or_create_collection("news_articles")

def expand_query(query: str) -> str:
    return f"User is looking for news related to: {query}. Include any associated terms and political/economic context."

def get_query_embedding(query: str) -> List[float]:
    prompt = expand_query(query)
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=[prompt]
    )
    return response.data[0].embedding

def semantic_search(query: str, top_k: int = 5, distance_threshold: float = 0.5):
    embedding = get_query_embedding(query)

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"]
    )
    print(f"\n🔍 Query: {query}")
    print("Top results (with distances):")
    for doc, meta, dist in zip(results["documents"][0], results["metadatas"][0], results["distances"][0]):
        print(f"→ [{dist:.3f}] {meta['title']}")
    matches = []
    for doc, meta, dist in zip(results["documents"][0], results["metadatas"][0], results["distances"][0]):
        if dist <= distance_threshold:
            matches.append({
                "title": meta["title"],
                "url": meta["url"],
                "summary": doc,
                "topics": meta["topics"],
                "distance": dist
            })

    return matches
