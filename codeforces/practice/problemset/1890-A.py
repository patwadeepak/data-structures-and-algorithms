# A. Doremy's Paint 3
# https://codeforces.com/problemset/problem/1890/A
from collections import Counter

def solve(a, n):
    c = Counter(a)
    k = list(c.keys())
    if len(k) > 2:
        print('No')
    else:
        if len(k) == 1:
            print('Yes')
        else:
            if n%2 == 0:
                if c[k[0]] == c[k[1]]:
                    print('Yes')
                else:
                    print('No')
            else:
                if c[k[0]] > c[k[1]]:
                    if c[k[0]] == 1 + c[k[1]]:
                        print('Yes')
                    else:
                        print('No')
                else:
                    if c[k[1]] == 1 + c[k[0]]:
                        print('Yes')
                    else:
                        print('No')

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        solve(a, n)

