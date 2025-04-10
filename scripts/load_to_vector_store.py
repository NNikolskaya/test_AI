import json

from news_ai.lang_vector_store import add_to_vector_store

with open("data/processed_articles.json", "r", encoding="utf-8") as f:
    articles = json.load(f)

add_to_vector_store(articles)
print("Articles added to Chroma vector store")