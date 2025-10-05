n, q = map(int, input().split())

lte = list(range(n+1))

fnzf = 1

for _ in range(q):
    x, y = map(int, input().split())
    if x < fnzf:
        print(0)
        continue
    upgraded = lte[x]
    fnzf = x
    for i in range(x+1, y):
        lte[i] -= upgraded
    print(upgraded)

"""
Seems correct solution.
But surprisingly gives TLE and WA as well.

Had a less optimized version before this 
but it was giving TLE.

After looking at the Solutions by TOP LGMs,
it seems that they implemented exact same solution
but since it was C++, it was fast enough to AC.

Update -
It was not unfair python TLE but it sure looked like it.
This is time my algo was too slow.

but for better or worse, I have decided to join the majority
and pick up C++ again. As I don't want to keep second guessing
if TLE was due to python slowness.
"""