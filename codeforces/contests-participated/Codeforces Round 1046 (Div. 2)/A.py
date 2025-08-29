def solve(a, b, c, d):
    x = min(a, b)
    y = max(a, b)
    if y <= (x + 1)*2:
        k = 1
        while k*c < a and k*d < b:
           k += 1 
        c *= k
        d *= k
        p = min(c-a, d-b)
        q = max(c-a, d-b)
        if q <= (p + 1)*2:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        a, b, c, d = list(map(int, input().split(' ')))
        solve(a, b, c, d)
