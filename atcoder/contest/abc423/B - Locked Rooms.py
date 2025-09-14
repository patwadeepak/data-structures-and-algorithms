def solve(n, l):
    acc = set([0])
    for r in range(1, n+1):
        if l[r-1] == 0:
            acc.add(r)
        else:
            break

    acc.add(n)
    for r in range(n-1, 0, -1):
        if l[r] == 0:
            acc.add(r)
        else:
            break
    
    return n + 1 - len(acc)

if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split(' ')))
    print(solve(n, l))
