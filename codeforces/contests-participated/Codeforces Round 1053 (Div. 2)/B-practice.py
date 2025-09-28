def solve(n, m, s, a):
    a = set(a)

    p = 1

    for i in range(n):
        if s[i] == 'A':
            p = p + 1
            a.add(p)
        else:
            while p+1 in a:
                p += 1
            p += 1
            a.add(p)
            while p+1 in a:
                p += 1
            p += 1

    print(len(a))
    a = list(a)
    a.sort()
    print(*a)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, m  = list(map(int, input().split()))
        s = input()
        a  = list(map(int, input().split()))
        solve(n, m, s, a)
"""
Beautiful solution creafted by me without editorial help.
Why can't I craft such elegant solutions in the contest ?
Need practice.
"""