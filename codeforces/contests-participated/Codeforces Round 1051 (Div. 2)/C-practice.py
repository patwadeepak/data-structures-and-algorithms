from collections import defaultdict

def dfs(n, g, node, s, vis, arr):
    if node in vis:
        return
    s.append(node)
    childs = g.get(node, [])
    for child in childs:
        dfs(n, g, child, s, vis, arr)
    item = s.pop()
    vis.add(item)
    arr.append(item)

def topsort(n, g, roots):
    op = []

    s = []
    vis = set()
    for root in roots:
        dfs(n, g, root, s, vis, op)
    return op[::-1]

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        g = defaultdict(list)
        all = set()
        child = set()
        n = int(input())
        for j in range(n-1):
            u, v, x, y = list(map(int, input().split(' ')))

            all.add(u)
            all.add(v)
            
            if x <= y:
                g[u].append(v)
                child.add(v)
            else:
                g[v].append(u)
                child.add(u)

        # multiple roots possible since not a binary tree but a generic tree
        roots = all - child
        op = topsort(n, g, roots)

        ans = [0]*n
        for i, v in enumerate(op, start=1):
            ans[v-1] = i
        print(*ans)
