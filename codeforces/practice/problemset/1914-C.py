def solve(n, k, a, b):
    b_maxx = float('-inf')
    res = float('-inf')
    s = 0

    for i in range(k):
        if i > len(a)-1:
            break
        if b[i] > b_maxx:
            b_maxx = b[i]
        s += a[i]
        res = max(res, s + b_maxx*(k-1-i))
    
    print(res)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, k = list(map(int, input().split(' ')))
        a = list(map(int, input().split(' ')))
        b = list(map(int, input().split(' ')))
        solve(n, k, a, b)
