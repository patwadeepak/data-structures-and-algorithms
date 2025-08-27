def explore(g, node, stack, depth):
    stack.add(node)
    conn_nodes = g[node]
    maxDepthNode = (float('-inf'), -1)
    for conn_node in conn_nodes:
        if conn_node not in stack:
            d, w = explore(g, conn_node, stack, depth+1)
            if d > maxDepthNode[0]:
                maxDepthNode = (d, w)

    if maxDepthNode[1] != -1:
        return maxDepthNode
    else:
        return depth, node

def find_longest_path(g):
    all_nodes = list(g.keys())
    
    d1, w1 = explore(g, g[all_nodes[0]][0], set(), 1)
    d2, w2 = explore(g, w1, set(), 1)

    print((w1, w2), (d1, d2))


def solve(n):
    g = {}
    # Knowledge gap filled - for a connected tree, there are V-1 edges always.
    for _ in range(n-1):
        u, v = list(map(int, input().split(' ')))
        if u in g:
            g[u].append(v)
        else:
            g[u] = [v]
        
        if v in g:
            g[v].append(u)
        else:
            g[v] = [u]
        
    n1, n2 = find_longest_path(g)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        solve(n)

"""
Not a solution yet.
WIP - We have only used 2-DFS technique to find the longest path's length and the endpoints
of the longest path.

We will modify the code to give us all the nodes of the longest path.
Which will help us to figure out the a, b, c.
"""