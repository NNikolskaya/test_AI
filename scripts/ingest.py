import json
from news_ai.scraper import scrape_articles
from news_ai.summarizer import summarize_article

if __name__ == "__main__":
    TEST_URLS = []
    with open("data/article_urls.txt", "r", encoding="utf-8") as f:
        TEST_URLS.extend(line.strip() for line in f if line.strip())

    raw_articles = scrape_articles(TEST_URLS)
    enriched_articles = []

    for article in raw_articles:
        if article.get("text"):
            summary_data = summarize_article(article["text"])
            article.update(summary_data)
        enriched_articles.append(article)

    with open("data/processed_articles.json", "w", encoding="utf-8") as f:
        json.dump(enriched_articles, f, ensure_ascii=False, indent=2)

    print("Articles scraped, summarized, and saved to data/processed_articles.json")
