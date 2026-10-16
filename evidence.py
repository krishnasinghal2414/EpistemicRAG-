
import re

documents = [
    {
        "id": 1,
        "source": "Document A",
        "content": "The library opens at 9 AM."
    },
    {
        "id": 2,
        "source": "Document B",
        "content": "The library opens at 10 AM."
    },
    {
        "id": 3,
        "source": "Document C",
        "content": "The library closes at 6 PM."
    }
]

def get_words(text):
    return re.findall(r"\b[a-z0-9]+\b", text.lower())

def search_documents(query):
    query_words = set(get_words(query))
    results = []

    for document in documents:
        content_words = set(get_words(document["content"]))
        score = len(query_words & content_words)

        if score > 0:
            results.append({
                "document": document,
                "score": score
            })

    results.sort(key=lambda item: item["score"], reverse=True)
    return results

query = input("Ask a question: ")
results = search_documents(query)

for result in results:
    print("Source:", result["document"]["source"])
    print("Content:", result["document"]["content"])
    print("Score:", result["score"])
    print()

# git add .
# git commit -m "first"
# git push origin main