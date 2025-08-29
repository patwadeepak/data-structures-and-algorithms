# https://codeforces.com/problemset/problem/1901/A

def solve(n, x, a):
    maxx = max(2*(x-a[-1]), a[0])

    for i in range(1, n):
        maxx = max(a[i] - a[i-1], maxx)
    
    print(maxx)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, x = list(map(int, input().split(' ')))
        a = list(map(int, input().split(' ')))
        solve(n, x, a)
