def solve(a, n):
    ops = 0
    negs = 0

    mx = float('-inf')
    for ai in a:
        if ai < 0:
            negs += 1
            mx = max(mx, ai)
        elif ai == 0:
            ops += 1
    
    if negs%2 == 0:
        print(ops)
    else:
        print(abs(mx) + 1 + ops)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        solve(a, n)
