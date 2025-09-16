# A. Cut the Array

def solve(a, n):
    for l in range(1, n-1):
        for r in range(2, n):
            if l < r:
                p = sum(a[:l])%3
                m = sum(a[l:r])%3
                s = sum(a[r:])%3

                if p == m == s:
                    return (l, r)
                elif p != m and m != s and s != p:
                    return (l, r)
    return 0, 0 

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        l, r = solve(a, n)
        print(l, r)
