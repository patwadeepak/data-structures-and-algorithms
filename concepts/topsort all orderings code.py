from collections import defaultdict

def find_all_topological_sorts(num_vertices, edges):
    """
    Finds all possible topological sorts of a Directed Acyclic Graph (DAG).

    Args:
        num_vertices (int): The total number of vertices in the graph (labeled 0 to n-1).
        edges (list of lists): A list of edges, where each edge is a [u, v] pair
                               representing a directed edge from u to v.

    Returns:
        list of lists: A list containing all possible topological sort orderings.
    """
    # Step 1: Build the graph and calculate initial indegrees
    graph = defaultdict(list)
    indegrees = [0] * num_vertices
    for u, v in edges:
        graph[u].append(v)
        indegrees[v] += 1

    # This list will store all the valid topological sorts we find
    all_sorts = []
    
    # This list represents the current path being built
    path = []
    
    # A set or boolean array to keep track of nodes currently in our path
    visited = [False] * num_vertices

    # Start the backtracking process
    _backtrack(graph, path, indegrees, visited, all_sorts, num_vertices)
    
    return all_sorts

def _backtrack(graph, path, indegrees, visited, all_sorts, num_vertices):
    """
    The recursive helper function that performs the backtracking.
    """
    # A flag to check if we have found any candidate for the next position
    found_candidate = False

    # --- The "Choice" Part ---
    # Iterate through all vertices to find the next candidate
    for v in range(num_vertices):
        # A node is a candidate if its indegree is 0 and it's not already in our path
        if indegrees[v] == 0 and not visited[v]:
            
            # --- 1. Act ---
            # Add the candidate to the current path and mark it as visited
            path.append(v)
            visited[v] = True
            
            # --- 2. Update State ---
            # "Remove" this node by decrementing the indegree of its neighbors
            for neighbor in graph[v]:
                indegrees[neighbor] -= 1
            
            # --- 3. Recurse ---
            # Recursively call the function to find the next node in the sort
            _backtrack(graph, path, indegrees, visited, all_sorts, num_vertices)
            
            # --- 4. Backtrack (Undo the choice) ---
            # Restore the state to explore other possibilities
            
            # a. Un-update the state: Increment the indegree of its neighbors back
            for neighbor in graph[v]:
                indegrees[neighbor] += 1
            
            # b. Un-act: Remove the node from the path and un-visit it
            visited[v] = False
            path.pop()

            found_candidate = True

    # --- Base Case ---
    # If we couldn't find any new candidate and have explored all branches from this point,
    # we check if we've formed a complete topological sort.
    if not found_candidate:
        if len(path) == num_vertices:
            # We must add a copy of the path, otherwise the list will be
            # emptied by the backtracking process.
            all_sorts.append(path[:])

# --- Example Usage ---
if __name__ == "__main__":
    # Example from the previous explanation
    # Nodes: 0, 1, 2, 3
    # Edges: 0->1, 0->2, 1->3, 2->3
    
    num_nodes = 4
    edge_list = [
        [0, 1],
        [0, 2],
        [1, 3],
        [2, 3]
    ]

    print(f"Finding all topological sorts for a graph with {num_nodes} nodes.")
    all_orderings = find_all_topological_sorts(num_nodes, edge_list)

    print(f"Found {len(all_orderings)} possible topological sorts:")
    for i, ordering in enumerate(all_orderings):
        print(f"{i+1}: {ordering}")

    print("\n" + "="*30 + "\n")

    # A more complex example
    # Nodes: 0, 1, 2, 3, 4, 5
    # Edges: 5->2, 5->0, 4->0, 4->1, 2->3, 3->1
    num_nodes_2 = 6
    edge_list_2 = [
        [5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]
    ]
    
    print(f"Finding all topological sorts for a graph with {num_nodes_2} nodes.")
    all_orderings_2 = find_all_topological_sorts(num_nodes_2, edge_list_2)
    
    print(f"Found {len(all_orderings_2)} possible topological sorts:")
    for i, ordering in enumerate(all_orderings_2):
        print(f"{i+1}: {ordering}")

"""
The worst case run time for this algorithm is O(N!⋅(N+E))
So, Only this about using this if n < 14 or something.
Otherwise this algorithm is a non-starter for solving problems 
with N  >= 14 as it will give TLE.

Most likely the problem can be solved with some greedy approach
while figuring out the valid top sort orderings or something similar.
"""