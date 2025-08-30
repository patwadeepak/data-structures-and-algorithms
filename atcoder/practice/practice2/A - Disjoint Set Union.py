def has_cycle(ds, u, v):
    if not ds:
        return 0

    for set in ds:
        if u in set and v in set:
            return 1

    return 0

def merge(ds, u, v):
    u_set = None
    v_set = None

    for s in ds:
        if u in s:
            u_set = s
        if v in s:
            v_set = s

        if u_set is not None and v_set is not None:
            break

    if u_set is not None and u_set == v_set:
        return

    if u_set is None and v_set is not None:
        v_set.add(u)
    elif u_set is not None and v_set is None:
        u_set.add(v)
    elif u_set is not None and v_set is not None:
        ds.remove(v_set)
        ds.remove(u_set)
        ds.append(v_set.union(u_set))
    else:
        ds.append(set([u, v]))


if __name__ == '__main__':
    n, q = map(int, input().split())

    disjoint_sets = []
    for ti in range(q):
        t, u, v = map(int, input().split())
        if t == 1:
            cycle_present = has_cycle(disjoint_sets, u, v)
            print(cycle_present)
        else:
            merge(disjoint_sets, u, v)

"""
Although I know the tree/array method of tracking
disjoint sets and doing merge or detecting cycle.

I thought just for a change lets try the disjoint sets
as an uninitiated who does not know all that and see
if this works out. It works. But it will have much 
much worse Time Complexity due to list.remove being O(n)
in python. We could try to fix this with smart techniques
keeping the logic as is but using tree/array method is way
better here.
"""
