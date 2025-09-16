from collections import Counter

def solve(a, n):
    if n <= 1:
        return 0

    c = Counter(a)
    multi_zeros = c[0] > 1

    if c[0] == n:
        return n

    l = 0
    r = n-1

    moved = True
    while l <= r and moved and l <= n-1 and r >= 0:
        moved = False
        if a[l] == l+1 or (a[l] == 0 and not multi_zeros):
            l += 1
            moved = True

        if a[r] == r+1 or (a[r] == 0 and not multi_zeros):
            r -= 1
            moved = True
    
    return max(r - l + 1, 0)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        op = solve(a, n)
        print(op)
