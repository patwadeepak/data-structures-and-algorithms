# C. The Nether
import sys

def pprint(*args):
    print(*args)
    sys.stdout.flush()

def make_query(x, portals):
    pprint(f'? {x} {len(portals)}', ' '.join(map(str, portals)))

def output_result(path):
    pprint(f'! {len(path)}',  ' '.join(map(str, path)))

def solve(n):
    k = 0
    d = {}
    path = []
    biggest = float('-inf')
    while k < n:
        k += 1
        make_query(k, list(range(1, n+1)))
        portals_travelled = int(input())
        if portals_travelled in d:
            d[portals_travelled].append(k)
        else:
            d[portals_travelled] = [k]

        if biggest < portals_travelled:
            path = [k]        
            biggest = portals_travelled

    for depth in range(biggest - 1, 0, -1):
        for c in d[depth]:
            make_query(path[-1], [path[-1], c])
            result = int(input())
            if result == 2:
                path.append(c)
                break
    
    output_result(path)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        solve(n)

"""
Turns out I got wrecked with this problem since I had never seen an interactive problem before.
The problem itself was kind of okay difficulty only.
"""