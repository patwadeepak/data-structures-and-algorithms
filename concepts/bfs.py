from collections import deque

def bfs(graph, start_node):
    # A set to keep track of visited nodes
    visited = set()
    # The queue for the BFS traversal
    queue = deque([start_node])

    # Process the starting node
    visited.add(start_node)

    while queue:
        # Pop the first node from the queue
        current_node = queue.popleft()
        # print(current_node, end=" ")

        # Add all unvisited neighbors to the queue
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

if __name__ == '__main__':
    # Example Usage
    # The graph is the same as the DFS example
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    bfs(graph, 'A') # Expected output: A B C D E F
