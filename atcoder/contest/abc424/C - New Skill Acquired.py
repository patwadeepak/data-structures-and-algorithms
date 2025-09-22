import sys
sys.setrecursionlimit(10**9)

def dfs(g, root, vis):
    if root in vis:
        return
    vis.add(root)
    childs = g.get(root, [])
    for child in childs:
        dfs(g, child, vis)

if __name__=='__main__':
    n = int(input())
    roots = set()
    g = {}

    for i in range(1, n+1):
        a, b = map(int, input().split(' '))
        if a == 0 and b == 0:
            g[i] = []
            roots.add(i)
        else:
            arr = g.get(a, [])
            arr.append(i)
            g[a] = arr

            arr = g.get(b, [])
            arr.append(i)
            g[b] = arr

    roots = list(roots)
    vis = set()
    i = 0
    while i <= len(roots)-1:
        root = roots[i]
        dfs(g, root, vis)
        i += 1

    print(len(vis))
