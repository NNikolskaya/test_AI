import json
from news_ai.scraper import scrape_articles
from news_ai.summarizer import summarize_article

TEST_URLS = [
    "https://www.bbc.com/news/articles/c7vnnd89e0jo",
    "https://edition.cnn.com/2025/04/09/entertainment/noah-wyle-jennifer-hudson-show/index.html",
]

if __name__ == "__main__":
    raw_articles = scrape_articles(TEST_URLS)
    enriched_articles = []

    for article in raw_articles:
        if article.get("text"):
            summary_data = summarize_article(article["text"])
            article.update(summary_data)
        enriched_articles.append(article)

    with open("data/processed_articles.json", "w", encoding="utf-8") as f:
        json.dump(enriched_articles, f, ensure_ascii=False, indent=2)

    print("✅ Articles scraped, summarized, and saved to data/processed_articles.json")
