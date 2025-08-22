# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
class Solution:

    # needs to have V first in a separate line and then start Edges from next line.
    def scan(self):
        adj = []
        for _ in range(V):
            edge = tuple(map(int, input(' ').split()))
            adj.append(edge)

        V, E = adj[0]

        return V, E, adj[1:]


    def find_root(self, parent, vertex):
        while parent[vertex] >= 0:
            vertex = parent[vertex]
        return vertex


    # Function to detect cycle using DSU in an undirected graph.
    def isCycle(self, V, edges):
        parent = [-1] * V

        for edge in edges:
            u, v = edge

            if parent[u] == -1 and parent[v] == -1:
                parent[v] = u
                parent[u] = -2

            elif parent[v] == -1:
                parent[v] = u
                root_u = self.find_root(parent, u)
                parent[root_u] = parent[root_u] - 1
            
            elif parent[u] == -1:
                parent[u] = v
                root_v = self.find_root(parent, v)
                parent[root_v] = parent[root_v] - 1

            else:
                root_u = self.find_root(parent, u)
                root_v = self.find_root(parent, v)

                if root_u == root_v:
                    # cycle is there
                    return True
                else:
                    # perform union attaching smaller component to the bigger one
                    if parent[root_u] > parent[root_v]:
                        parent[root_u] = root_v
                        parent[root_v] = parent[root_v] - 2
                    else:
                        parent[root_v] = root_u
                        parent[root_u] = parent[root_u] - 2

        return False


# driver code
if __name__ == '__main__':

    # # Has cycle
    # edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
    # V, E = 4, 4

    # does not have cycle
    # edges = [[0, 1], [1, 2], [2, 3]]
    # V, E = 4, 3

    V, E = 6, 6
    edges = [
        [0, 1],
        [1, 2],
        [1, 3],
        [2, 4],
        [3, 4],
        [4, 5],
    ]

    s = Solution()
    # V, E, adj = s.scan()
    result = s.isCycle(V, edges)
    print('Cycle was', 'not' if not result else '\b','detected in the Graph')

# Passed all test cases now. Hurray ! :). I will be a red coder soon.