class Solution:

    def scan(self):
        V = int(input())
        adj = []
        for v in range(V):
            edge = tuple(map(int, input(' ').split()))
            adj.append(edge)
        return V, adj

    # Function to detect cycle using DSU in an undirected graph.
    def detectCycle(self, V, adj):
        pass

# driver code
if __name__ == '__main__':

    adj = [
        (5, 5),
        (0, 2), 
        (0, 3), 
        (0, 4), 
        (1, 3), 
        (2, 4),
    ]
    V = len(adj)
    
    s = Solution()
    # V, adj = s.scan()
    s.detectCycle(V, adj)
