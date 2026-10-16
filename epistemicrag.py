
import re

documents = [
    {
        "id": "D1",
        "source": "Library Schedule",
        "content": "The library opens at 9 AM. It closes at 6 PM."
    },
    {
        "id": "D2",
        "source": "Updated Library Notice",
        "content": "The library opens at 10 AM. It is closed on Sunday."
    },
    {
        "id": "D3",
        "source": "Garden Notice",
        "content": "The garden opens at 7 AM. It closes at 5 PM."
    }
]


def get_words(text):
    return set(re.findall(r"\b[a-z0-9]+\b", text.lower()))


def search_documents(query):
    query_words = get_words(query)
    results = []

    for document in documents:
        content_words = get_words(document["content"])
        score = len(query_words & content_words)

        if score > 0:
            results.append({
                "document": document,
                "score": score
            })

    results.sort(key=lambda item: item["score"], reverse=True)
    return results


def extract_claims(document_id, text, start_number):
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    claims = []

    for sentence in sentences:
        sentence = sentence.strip()

        if sentence:
            claims.append({
                "id": "C" + str(start_number + len(claims)),
                "document_id": document_id,
                "text": sentence
            })

    return claims


def build_graph(retrieved_documents, claims):
    graph = {}

    for document in retrieved_documents:
        document_id = document["id"]
        graph[document_id] = []

        for claim in claims:
            if claim["document_id"] == document_id:
                graph[document_id].append(claim["id"])
                graph[claim["id"]] = []

    return graph


def has_cycle(graph):
    visited = set()
    active = set()

    def dfs(node):
        if node in active:
            return True

        if node in visited:
            return False

        visited.add(node)
        active.add(node)

        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True

        active.remove(node)
        return False

    for node in graph:
        if dfs(node):
            return True

    return False


query = input("Ask a question: ")

results = search_documents(query)

if not results:
    print("No matching documents found.")

else:
    retrieved_documents = []
    all_claims = []

    for result in results:
        document = result["document"]
        retrieved_documents.append(document)

        new_claims = extract_claims(
            document["id"],
            document["content"],
            len(all_claims) + 1
        )

        all_claims.extend(new_claims)

    print("\nRETRIEVED DOCUMENTS")

    for result in results:
        document = result["document"]
        print("\nDocument ID:", document["id"])
        print("Source:", document["source"])
        print("Content:", document["content"])
        print("Score:", result["score"])

    print("\nEXTRACTED CLAIMS")

    for claim in all_claims:
        print("\nClaim ID:", claim["id"])
        print("Claim:", claim["text"])
        print("Source Document:", claim["document_id"])

    graph = build_graph(retrieved_documents, all_claims)

    print("\nDAG EDGES")

    for document_id in graph:
        for claim_id in graph[document_id]:
            print(document_id, "--supports/source-->", claim_id)

    print("\nDAG VALIDATION")

    if has_cycle(graph):
        print("Invalid DAG: cycle detected")
    else:
        print("Valid DAG: no cycles detected")
