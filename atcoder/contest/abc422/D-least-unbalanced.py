def solve():
    n, k = map(int, input().split(' '))
    n = (2**n)
    r = k%n
    q = k//n

    res = []
    start = [q]*int((n - 2*r)/2)
    middle = [q, q+1]*r

    res.extend(start)
    res.extend(middle)
    res.extend(start)

    if r > 0:
        print(r%2)
    else:
        print(0)
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    solve()