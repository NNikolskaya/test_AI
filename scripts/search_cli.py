from news_ai.search import semantic_search

if __name__ == "__main__":
    print("Semantic search over your news collection")
    query = input("Enter your query: ")

    results = semantic_search(query)

    if not results:
        print("\nNo relevant articles found.")
    else:
        for i, article in enumerate(results, 1):
            print(f"* Result {i} (distance: {article['distance']:.3f})")
            print(f"Title  : {article['title']}")
            print(f"URL    : {article['url']}")
            print(f"Topics : {article['topics']}")
            print(f"Summary:\n{article['summary']}")
