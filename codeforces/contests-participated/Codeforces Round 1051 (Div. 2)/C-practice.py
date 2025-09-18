from collections import defaultdict

def topsort(n, g, root):
    return []

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        g = defaultdict(list)
        all_set = set()
        not_root = set()
        n = int(input())
        for j in range(n-1):
            u, v, x, y = list(map(int, input().split(' ')))

            all_set.add(u)
            all_set.add(v)
            
            if x > y:
                g[u].append(v)
                not_root.add(v)
            else:
                g[v].append(u)
                not_root.add(u)
        
        root = list(all_set - not_root)[0]
        print(topsort(n, g, root))

"""
WIP: Need to work on the topological sort for this problem
"""