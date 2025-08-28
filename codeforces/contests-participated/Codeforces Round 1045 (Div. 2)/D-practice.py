import traceback
def explore(g, node, stack, depth, path):
    if node not in path:
        path.append(node)
    stack.add(node)
    conn_nodes = g[node]
    maxDepthNode = (float('-inf'), -1, [])
    for conn_node in conn_nodes:
        if conn_node not in stack:
            d, w, p = explore(g, conn_node, stack, depth+1, path)
            if d > maxDepthNode[0]:
                maxDepthNode = (d, w, p)

    if maxDepthNode[1] != -1:
        return maxDepthNode
    else:
        return depth, node, tuple(path)

def find_longest_path(g):
    all_nodes = list(g.keys())

    i = 0
    while len(g[all_nodes[i]]) <= 0:
        i+=1
 
    _, w1, _ = explore(g, g[all_nodes[i]][0], set(), 1, [])
    _, _, path = explore(g, w1, set(), 1, [])

    return path

def solve(n):
    if n == 1:
        return (-1,)

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
        
    path = find_longest_path(g)

    if len(path) == n:
        return (-1,)

    edge_counts = [(len(g[num])-2, num) for num in path]
    edge_counts[0]  = (edge_counts[0][0]+1, edge_counts[0][1])
    edge_counts[-1] = (edge_counts[-1][0]+1, edge_counts[-1][1])
 
    a, b, c = -1, -1, -1
    for i in range(len(edge_counts)):
        if edge_counts[i][0] > 0:
            b = edge_counts[i][1]

            if i > 1:
                a = edge_counts[i-1][1]
            else:
                a = edge_counts[i+1][1]

            j = 0
            c = g[b][j]
            while c == a or c in path:
                j += 1

                if j>=len(g[b]):
                    c = -1
                    break

                c = g[b][j]
 
        if a != -1 and b != -1 and c != -1:
            break

    return (a, b, c)

if __name__ == '__main__':
    t = int(input())

    try:
        for i in range(1, t+1):
            n = int(input())
            out = solve(n)

            if i == t:
                print(*out, end='')
            else:
                print(*out)
    except Exception:
        traceback_str = traceback.format_exc()
        if len(traceback_str.splitlines()) >= 3:
            print('\n'.join((traceback_str.splitlines()[-4:])))
        else:
            print(traceback_str)

"""
Very Close but not quite there.
It turns out that my dfs is not giving correct longest tree right now.
There are bugs in it.
"""