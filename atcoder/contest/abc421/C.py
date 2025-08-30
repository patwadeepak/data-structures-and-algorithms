def solve(s, n):
    A = []
    B = []

    for i, ch in enumerate(s):
        if ch == 'A':
            A.append(i)
        else:
            B.append(i)

    ops1 = 0
    for i, bi in zip(range(0, 2*n, 2), B):
        ops1 += abs(bi - i)
    
    ops2 = 0
    for i, bi in zip(range(1, 2*n, 2), B):
        ops2 += abs(bi - i)
    
    print(min(ops1, ops2))


if __name__ == '__main__':
    n = int(input())
    s = input()
    solve(s, n)
