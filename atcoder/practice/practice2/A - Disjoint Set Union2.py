
def find_root(parent, vertex):
    while parent[vertex] >= 0:
        vertex = parent[vertex]
    return vertex


# Function to detect cycle using DSU in an undirected graph.
def isCycle(parent, u, v):
    root_u = find_root(parent, u)
    root_v = find_root(parent, v)

    if root_u == root_v:
        # cycle is there
        return True

    return False


def merge(parent, u, v):
    root_u = find_root(parent, u)
    root_v = find_root(parent, v)
    if root_u == root_v:
        return
    if parent[root_u] > parent[root_v]:
        parent[root_u] = root_v
        parent[root_v] = parent[root_v] - 2
    else:
        parent[root_v] = root_u
        parent[root_u] = parent[root_u] - 2


if __name__ == '__main__':
    n, q = map(int, input().split())

    parent = [-1] * n
    for ti in range(q):
        t, u, v = map(int, input().split())
        if t == 1:
            cycle_present = isCycle(parent, u, v)
            print(1 if cycle_present else 0)
        else:
            merge(parent, u, v)
