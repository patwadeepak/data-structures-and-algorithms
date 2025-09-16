def solve(a, b, n):
    if n == 1:
        print(2)
        return

    m = 1
    s = 0

    if a[0] > b[0]:
        a[0], b[0] = b[0], a[0]
        s += 1
    elif a[0] == b[0]:
        m *= 2

    for i in range(1, n):
        if a[i] == b[i]:
            m *= 2
        elif a[i-1] <= a[i] and b[i-1] < b[i]:
            if a[i-1] < b[i] and b[i-1] < a[i]:
                m *= 2
            else:
                s += 1
    subsets = s * m
    print(subsets%998244353)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        b = list(map(int, input().split(' ')))
        solve(a, b, n)
