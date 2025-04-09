# 📰 News AI Summarizer & Semantic Search

This project extracts news from URLs, summarizes them using GPT, identifies main topics, and stores everything in a vector database to enable powerful **semantic search**.

Built with Python, OpenAI API, and ChromaDB.

---

## Features

- Scrape full article text and title from URLs
- Generate a **summary** and **main topics** using OpenAI GPT
- Create vector embeddings via `text-embedding-ada-002`
- Store articles in Chroma vector DB
- Search articles semantically by user queries (e.g. `"Trump tariffs"` returns relevant content even if those exact words aren’t used)
- Results are filtered by semantic closeness (`distance < 0.5`)

---

## Tech Stack

- Python 3.13+
- [Poetry](https://python-poetry.org/)
- `openai`, `chromadb`, `newspaper3k`, `dotenv`

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/news-ai-search.git
cd news-ai-search
```
### 2. Install dependencies
```bash
poetry install
```
### 3. Set up OpenAI API key
Create .env file in the root directory:

OPENAI_API_KEY=sk-...

### 4. Add article URLs to data/article_urls.txt
   Each line should be a news article URL.
   
### 5. Run ingestion pipeline
```bash
poetry run python scripts/ingest.py
```
This will:
1. Scrape articles
2. Generate summaries & topics
3. Save processed data to data/processed_articles.json

### 6. Load articles into vector DB
```bash
poetry run python scripts/load_to_vector_store.py
```

## Semantic Search CLI
```bash
poetry run python scripts/search_cli.py
```

You can enter free-text queries like:

>Enter your query: US-China trade war

Sample output:

>🔸 Result 1 (distance: 0.354)
Title  : Is the US making $2bn from tariffs
URL    : https://example.com/article123
Topics : Tariffs, Trade deficits, Canada dairy tariffs, US-EU car imports
Summary:
President Trump has claimed that the US is collecting billions of dollars...

## How It Works
Scraping — Full text via newspaper3k

Summarization — GPT-3.5-turbo summarizes and detects topics

Embedding — text-embedding-ada-002 converts summary+topics to vector

Storage — ChromaDB stores vector and metadata

Search — Query embedded and compared to stored vectors (cosine similarity)

## Folder structure
news_ai/
\
├── scraper.py            # HTML article extraction
\
├── summarizer.py         # GPT-based summarization
\
├── vector_store.py       # Chroma vector DB logic
\
├── search.py             # Semantic search logic

scripts/
\
├── ingest.py             # End-to-end ETL from URLs
\
├── load_to_vector_store.py 
\
├── search_cli.py         # Command line search interface


## Notes
**Note: Although LlamaIndex was listed among the recommended libraries, in practice it was found that the similarity score it returns during vector search does not correlate well with actual relevance. For better stability and accuracy, direct search via ChromaDB was implemented instead.**