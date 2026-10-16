
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
        "content": "The library opens at 9 AM."
    }
]

claims = [
    {
        "id": "C1",
        "text": "The library opens at 9 AM.",
        "document_ids": [1, 3]
    },
    {
        "id": "C2",
        "text": "The library opens at 10 AM.",
        "document_ids": [2]
    }
]

for claim in claims:
    print("Claim:", claim["text"])

    for document_id in claim["document_ids"]:
        for document in documents:
            if document["id"] == document_id:
                print("Supported by:", document["source"])

    print()
