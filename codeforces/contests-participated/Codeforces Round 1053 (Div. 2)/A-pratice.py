# https://codeforces.com/contest/2151/problem/A

def solve(a, n, m):
    for i in range(m-2, -1, -1):
        if a[i+1] == 1:
            return 1
    return n - a[-1] + 1

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, m = list(map(int, input().split()))
        a = list(map(int, input().split()))
        print(solve(a, n, m))
