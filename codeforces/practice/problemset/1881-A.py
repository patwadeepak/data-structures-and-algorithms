def solve(x, s, n, m):
    ops = 0
    found = False
    while True:
        if s not in x:
            if ops >= 5:
                break
            x += x
            ops += 1
        else:
            found = True
            break
    
    print(-1 if not found else ops)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, m = list(map(int, input().split(' ')))
        x = input()
        s = input()
        solve(x, s, n, m)
