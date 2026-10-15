
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

for document in documents:
    print(document["source"])
    print(document["content"])
    print()

count_9 = 0
count_10 = 0

for document in documents:
    if "9 AM" in document["content"]:
        count_9 += 1

    if "10 AM" in document["content"]:
        count_10 += 1

print("Evidence for 9 AM:", count_9)
print("Evidence for 10 AM:", count_10)
