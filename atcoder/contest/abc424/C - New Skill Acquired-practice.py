import sys
sys.setrecursionlimit(10**9)

vis = None
g = None

def dfs(node):
    vis[node] = 1
    children = g[node]
    for child in children:
        if vis[child] != 1:
            dfs(child)

if __name__=='__main__':
    n = int(input())
    g = [[] for _ in range(n+1)]
    vis = [0]*(n+1)
    vis[0] = 1

    for i in range(1, n+1):
        a, b = map(int, input().split())
        g[a].append(i)
        g[b].append(i)

    dfs(0)

    print(sum(vis)-1)

"""
Turns out even editorial provided solution got TLE when using PyPy on Atcoder.
I switched to CPython and then only it got AC
"""
