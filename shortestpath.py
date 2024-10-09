from collections import deque


def bfs_shortest_path(graph, start, goal):
    visited = set()  # To keep track of visited nodes
    queue = deque([(start, [start])])  # Queue to hold (node, path)

    while queue:
        current_node, path = queue.popleft()  # Dequeue a node and its path

        if current_node == goal:
            return path  # Return the path to the goal

        if current_node not in visited:
            visited.add(current_node)  # Mark the node as visited

            # Add all unvisited neighbors to the queue with the updated path
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None  # Return None if no path found


# Example graph represented as an adjacency list
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

# Find the shortest path from 'A' to 'F'
shortest_path = bfs_shortest_path(graph, "A", "F")
print("Shortest path from A to F:", shortest_path)
