
nodes = {
    "D1": "Document A",
    "D2": "Document B",
    "D3": "Document C",
    "C1": "Library opens at 9 AM",
    "C2": "Library opens at 10 AM"
}

edges = [
    ("D1", "C1", "supports"),
    ("D3", "C1", "supports"),
    ("D2", "C2", "supports"),
    ("C1", "C2", "contradicts")
]

for start, end, relation in edges:
    print(nodes[start], "--", relation, "-->", nodes[end])
