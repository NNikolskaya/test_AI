from newspaper import Article
from typing import List, Dict
from tqdm import tqdm


def scrape_article(url: str) -> Dict[str, str]:
    try:
        article = Article(url)
        article.download()
        article.parse()
        return {
            "url": url,
            "title": article.title,
            "text": article.text,
        }
    except Exception as e:
        return {
            "url": url,
            "title": "",
            "text": "",
            "error": str(e),
        }


def scrape_articles(urls: List[str]) -> List[Dict[str, str]]:
    results = []
    for url in tqdm(urls, desc="Scraping articles"):
        result = scrape_article(url)
        results.append(result)
    return results
