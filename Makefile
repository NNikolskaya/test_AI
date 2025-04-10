load_data:
	poetry run python scripts/process_and_index.py

search:
	poetry run python scripts/lang_search.py

streamlit:
	poetry run streamlit run scripts/streamlit_search.py

load_articles:
    poetry run python scripts/ingest.py

load_embeddings:
    poetry run python scripts/load_to_vector_store.py

stop-streamlit:
	@echo "🔻 Stopping Streamlit..."
	@pkill -f streamlit || echo "Streamlit was not running."