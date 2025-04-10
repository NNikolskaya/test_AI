from news_ai.lang_vector_store import add_to_vector_store
from news_ai.scraper import scrape_articles
from news_ai.summarizer import enrich_with_genai
import json
from pathlib import Path

def main():
    url_file = Path("data/article_urls.txt")
    if not url_file.exists():
        print("URL file not found.")
        return

    with url_file.open("r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    if not urls:
        print("No URLs found in the file.")
        return

    print(f"Found {len(urls)} URLs to process...")

    articles = scrape_articles(urls)
    print(f"Scraped {len(articles)} articles.")

    enriched = enrich_with_genai(articles)
    print(f"Summarized and tagged {len(enriched)} articles.")

    add_to_vector_store(enriched)
    print("Embedded and indexed all articles.")

    # Save locally for reference
    with open("data/processed_articles.json", "w", encoding="utf-8") as f:
        json.dump(enriched, f, ensure_ascii=False, indent=2)

    print("Done! Everything saved and ready for search.")

if __name__ == "__main__":
    main()
