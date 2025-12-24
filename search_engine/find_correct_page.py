from user_search import get_query_keywords
from load_pages import load_pages

query_keywords = get_query_keywords()
pages = load_pages()

results = []

for page, keywords in pages.items():
    score = len(set(query_keywords) & set(keywords))
    if score > 0:
        results.append((page, score))

results.sort(key=lambda x: x[1], reverse=True)

print("\nresults:\n")
for page, score in results:
    print(f"{page}")
