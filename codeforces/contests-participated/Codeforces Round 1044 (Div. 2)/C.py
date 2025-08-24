# C. The Nether
import sys

def pprint(*args):
    print(*args)
    sys.stdout.flush()

def make_query(x, portals):
    pprint(f'? {x} {len(portals)}', ' '.join(map(str, portals)))

def solve(n):
    k = 0
    while k < 2*n:
        k += 1


if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        solve(n)

"""
First time faced an interactive problem.
Got over it but realized that problem has a DAG
and my graph theory is limited to to finding cycles using disjoint sets only.

Will try solving this after competition.
"""