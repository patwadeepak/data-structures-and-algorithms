def dfs(graph, start_node):
    # A set to keep track of visited nodes to avoid cycles
    visited = set()
    # The stack for the DFS traversal
    stack = [start_node]

    # track depth and parent
    d = { key: -1  for key in graph.keys() }
    p = { key: -1  for key in graph.keys() }

    # farthest node tracking
    farthest_node = start_node

    # distance form farthest node
    d[start_node] = 0

    while stack:
        # Pop the last node from the stack
        current_node = stack.pop()
        
        # Process the node if it hasn't been visited
        if current_node not in visited:
            # print(current_node, end=" ")
            if d[current_node] > d[farthest_node]:
                farthest_node = current_node

            visited.add(current_node)
            
            # Push neighbors onto the stack. We reverse the list to ensure we visit them in a consistent order.
            # Without reverse(), the order can be unpredictable depending on the graph's representation.
            for neighbor in reversed(graph[current_node]):
                if neighbor not in visited:
                    d[neighbor] = d[current_node] + 1
                    p[neighbor] = current_node
                    stack.append(neighbor)

    return d, p


if __name__ == '__main__':
    # Example Usage
    # The graph is represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['F', 'A'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C']
    }

    d1, _ = dfs(graph, 'A')

    maxDepth = -1
    u = None
    for key, value in d1.items():
        if value > maxDepth:
            u = key
            maxDepth = value

    d2, p2 = dfs(graph, u)

    maxDepth = -1
    v = None
    for key, value in d2.items():
        if value > maxDepth:
            v = key
            maxDepth = value

    # diameter of tree will be 
    path = []
    currNode = v
    while True:
        path.append(currNode)
        if currNode == u:
            break
        currNode = p2[currNode]
    
    print(*path)
