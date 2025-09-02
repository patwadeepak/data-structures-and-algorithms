from collections import Counter

def solve(s, n):
    c = Counter(s)
    ans = len(c.keys())

    s = s[::-1]

    for i in range(n):
        c[s[i]] -= 1
        for k, v in c.items():
            if v > 0:
                ans += 1

    print(ans)


if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        s = input()
        solve(s, n)
