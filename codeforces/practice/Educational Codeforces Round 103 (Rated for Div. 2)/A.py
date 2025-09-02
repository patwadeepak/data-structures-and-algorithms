import math

def solve(n, k):
    if n <= k:
        print(k//n + (1 if k%n != 0 else 0))
    else:
        d = math.ceil(n/k)
        k = k*d
        print(k//n + (1 if k%n != 0 else 0))

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, k = list(map(int, input().split(' ')))
        solve(n, k)
