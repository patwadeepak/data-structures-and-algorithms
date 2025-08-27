def solve(a, n):
    ops = 0
    for i in range(n):
        if i%2 == 0: # index even but actually odd by 1 indexing
            if i+1 < n and a[i] > a[i+1]:
                ops += a[i] - a[i+1]
                a[i] = a[i+1]
            if i >= 2 and a[i-1] < a[i-2]+a[i]:
                diff = a[i-2]+a[i]-a[i-1]
                a[i] -= diff
                ops += diff
        else:
            if i+1 < n and a[i] < a[i+1]:
                ops +=  a[i+1] - a[i]
                a[i+1] = a[i]

    print(ops)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        solve(a, n)
