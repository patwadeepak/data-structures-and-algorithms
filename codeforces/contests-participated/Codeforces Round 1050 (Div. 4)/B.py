def solve(n, m, x, y, a, b):
    crossing = 0
    for ai in a:
        if ai < y:
            crossing += 1
        else:
            break

    for bi in b:
        if bi < x:
            crossing += 1
        else:
            break
    
    return crossing

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, m, x, y = list(map(int, input().split(' ')))
        a = list(map(int, input().split(' ')))
        b = list(map(int, input().split(' ')))
        output = solve(n, m, x, y, a, b)
        print(output)
