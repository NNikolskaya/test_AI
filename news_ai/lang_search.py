from langchain_chroma import Chroma
from news_ai.config import Config


def semantic_search(query: str, k: int = 5, distance_threshold: float = 0.5):
    db = Chroma(persist_directory=Config.CHROMA_PATH, embedding_function=Config.embedding)
    results = db.similarity_search_with_score(query, k=k)

    filtered = []
    for doc, score in results:
        if score < distance_threshold:
            filtered.append({
                "title": doc.page_content.split("\n")[0].replace("Title: ", ""),
                "summary": doc.page_content,
                "url": doc.metadata["url"],
                "score": score
            })
    return filtered
