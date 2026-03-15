from collections import deque


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}


# DFS using stack
def dfs(start):

    stack = [start]
    visited = set()

    while stack:

        node = stack.pop()

        if node not in visited:
            print(node)

            visited.add(node)

            stack.extend(graph[node])


# BFS using queue
def bfs(start):

    queue = deque([start])
    visited = set()

    while queue:

        node = queue.popleft()

        if node not in visited:
            print(node)

            visited.add(node)

            queue.extend(graph[node])


print("DFS:")
dfs("A")

print("\nBFS:")
bfs("A")