import sys
sys.setrecursionlimit(10**9)

# A corrected, standard DFS function.
# The 's' list is unnecessary and has been removed.
def dfs(g, node, vis):
    # 1. If we have already fully explored this node, stop.
    if node in vis:
        return
    
    # 2. Mark the node as visited immediately upon entry.
    # This is the key to avoiding TLE.
    vis.add(node)
    
    # 3. Explore all neighbors.
    children = g.get(node, [])
    for child in children:
        dfs(g, child, vis)

if __name__ == '__main__':
    n = int(input())
    # You can use a single list for roots instead of a set.
    roots = []
    g = {}

    for i in range(1, n + 1):
        a, b = map(int, input().split(' '))
        if a == 0 and b == 0:
            # This skill is initially learned.
            roots.append(i)
        else:
            # Build the graph correctly, without the i != a/b check.
            # If skill 'a' is learned, we might learn skill 'i'.
            # So, an edge goes from a -> i.
            arr_a = g.get(a, [])
            arr_a.append(i)
            g[a] = arr_a

            # Same for skill 'b'.
            arr_b = g.get(b, [])
            arr_b.append(i)
            g[b] = arr_b

    # A set to keep track of all visited/learned skills.
    vis = set()
    
    # Start a DFS from each initially learned skill.
    for root in roots:
        if root not in vis:
            dfs(g, root, vis)
            
    print(len(vis))