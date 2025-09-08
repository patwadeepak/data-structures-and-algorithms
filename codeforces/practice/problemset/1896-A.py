# A. Jagged Swaps
# https://codeforces.com/problemset/problem/1896/A

def solve(a, n):
    if a[0] != 1:
        print('NO')
    else:
        print('YES')

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        solve(a, n)

"""
This was too simple that I kept looking for pitfalls for a while
then finally had to give in and believe that this problem is
indeed too simple.
"""