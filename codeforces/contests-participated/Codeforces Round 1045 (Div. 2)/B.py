def solve(a, n, k):
    smallest = min(a)
    q = 1
    r = smallest + k*q

    for i, num in enumerate(a):
        j = 1
        while ((r*j) - num) % k != 0:
            j += 1

            if j > k:
                q += 1
                r = smallest + k*q
                j = 1
                continue

        a[i] = r*j
    
    print(' '.join(map(str, a)))

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, k = list(map(int, input().split(' ')))
        a = list(map(int, input().split(' ')))
        solve(a, n, k)

"NOT a solution but quite close"
"""
Turns out this rounds was highly unbalanced and problem C was simpler
than this problem B. And because of that even solving only A in the contest
got me an increase in the ratings.

Although I would liked if B was solved as well.
"""