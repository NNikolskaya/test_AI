from news_ai.lang_search import semantic_search

query = input("🔍 Enter your search query: ")
results = semantic_search(query)

print("\n🔎 Results:")
if not results:
    print("No relevant articles found.")
else:
    for r in results:
        print(f"\n— {r['title']}\n   URL: {r['url']}\n   🔹 Score: {r['score']:.3f}")
