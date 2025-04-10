import streamlit as st
from news_ai.lang_search import semantic_search

st.set_page_config(page_title="News Search with GenAI", layout="wide")
st.title("🧠 Smart News Search")
st.markdown("Search through summarized and tagged news articles using **semantic similarity**.")

query = st.text_input("🔍 Enter your search query")

if query:
    results = semantic_search(query)
    if not results:
        st.warning("No relevant articles found.")
    else:
        for item in results:
            st.markdown("----")
            st.markdown(f"### [{item['title']}]({item['url']})")
            st.markdown(f"**URL:** {item['url']}")
            st.markdown(f"**Similarity Score:** `{item['score']:.3f}`")
