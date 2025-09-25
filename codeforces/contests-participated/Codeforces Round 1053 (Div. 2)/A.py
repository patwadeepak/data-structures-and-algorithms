def solve(a, n, m):
    last = a[-1]
    crossed = 0
    for ai in a[:-1][::-1]:
        if ai == last-1:
            last = ai
        elif last == 1:
            crossed += 1
            last = a[-1] - crossed

    if crossed > 0:
        print(1)
    else:
        print(n - a[-1] + 1)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, m = list(map(int, input().split(' ')))
        a = list(map(int, input().split(' ')))
        solve(a, n, m)
