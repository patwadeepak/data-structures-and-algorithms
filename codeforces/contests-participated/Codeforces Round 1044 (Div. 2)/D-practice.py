# D. Chicken Jockey

def solve(a, n):
    if n == 1:
        if a[0] > 0:
            return a[0]
        else:
            return 0

    while n > 0:
        if a[n-1] < 1:
            a.pop()
        if a[n-1] == 1 and n <= len(a) - 1:
            a[n] -= (n-1)
            return 1 + solve(a[:n-1], len(a[:n-1])) + solve(a[n:], len(a[n:]))

        # last line
        n -= 1


if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        print(solve(a, n))
"""
This looks like a very very good problem to solve.
"""