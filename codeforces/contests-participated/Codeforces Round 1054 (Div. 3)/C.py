def solve(a, n, k):
    miss = 0
    ks = 0

    for ai in a:
        if ai == k:
            ks += 1

    a = set(a)
    for i in range(k):
        if i not in a:
            miss += 1

    if miss >= ks:
        print(miss)
    else:
        print(ks)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, k = list(map(int, input().split(' ')))
        a = list(map(int, input().split(' ')))
        solve(a, n, k)

"""
The solution is correct by output and even passed all pretests.
But it gave TLE after system testing. :(
"""