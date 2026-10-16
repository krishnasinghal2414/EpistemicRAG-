
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

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True

        active.remove(node)
        return False

    for node in graph:
        if dfs(node):
            return True

    return False


graph = {
    "D1": ["C1"],
    "C1": ["A1"],
    "A1": []
}

if has_cycle(graph):
    print("Invalid DAG: cycle detected")
else:
    print("Valid DAG: no cycles")
