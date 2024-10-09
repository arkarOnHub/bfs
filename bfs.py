from collections import deque


def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Queue for BFS

    while queue:
        node = queue.popleft()  # Dequeue a node
        if node not in visited:
            print(node, end=" ")  # Process the node (e.g., print it)
            visited.add(node)  # Mark the node as visited

            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


# Example graph represented as an adjacency list
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["F", "A"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

# Run BFS starting from node 'A'
bfs(graph, "C")
