from collections import deque
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        q = deque()
        res = []
        v = [False]*len(adj)
        
        v[0] = True
        q.append(0)
        
        while q:
            node = q.popleft()
            v[node] = True
            res.append(node)
            
            for child in adj[node]:
                if not v[child]:
                    q.append(child)
        return res

if __name__ == '__main__':
    s = Solution()
    graph = [[2, 3, 1], [0], [0, 4], [0], [2]]
    s.bfs(graph)
