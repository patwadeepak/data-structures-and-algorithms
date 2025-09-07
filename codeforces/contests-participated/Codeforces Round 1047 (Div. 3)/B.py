# https://codeforces.com/contest/2137/problem/B
# B. Fun Permutation

def solve(a, n):
    b = [n+1 - x for x in a]
    print(*b)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        solve(a, n)
