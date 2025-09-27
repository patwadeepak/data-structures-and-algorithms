def solve(a, n):
    a.sort()
    md = float('-inf')
    for i in range(0, n+1, 2):
        if n-i-2 >= 0 and n-i-1 <= n-1:
            d = a[n-i-1] - a[n-i-2]
            md = max(md, d)
    print(md)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        solve(a, n)
