def solve(a, n):
    s = set(a)
    set_sum  = sum(s)
    if set_sum != n:
        print(-1)
        return
    
    d = {}
    for i, num in enumerate(s, start=1):
        d[num] = i

    arr = []
    for num in a:
        arr.append(d[num])

    print(*arr)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        solve(a, n)
