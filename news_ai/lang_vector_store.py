from langchain_chroma import Chroma
from langchain.schema.document import Document
from news_ai.config import Config

def add_to_vector_store(articles):
    docs = []
    for article in articles:
        if article.get("summary") and article.get("topics"):
            content = f"Title: {article['title']}\nSummary: {article['summary']}\nTopics: {', '.join(article['topics'])}"
            metadata = {"url": article["url"]}
            docs.append(Document(page_content=content, metadata=metadata))

    Chroma.from_documents(docs, embedding=Config.embedding, persist_directory=Config.CHROMA_PATH)
