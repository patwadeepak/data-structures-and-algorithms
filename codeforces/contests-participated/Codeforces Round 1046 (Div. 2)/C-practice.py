# C. Against the Difference
from functools import cache

@cache
def get_freq(a, n):
    d = {}
    for i in range(len(a)):
        if a[i] in d:
            d[a[i]].append(i)
        else:
            d[a[i]] = [i]
    return d

def solve(a, n):
    if n <= 0:
        return 0
    if n == 1 and a == [1]:
        return 1

    f = get_freq(tuple(a), n)
    if len(f[a[-1]]) >= a[-1]:
        x = len(f[a[-1]]) - a[-1] - 1
        if x >= 0:
            return max(solve(a[:-1], n-1), solve(a[:x], len(a[:x])) + a[-1])
        else:
            return max(solve(a[:-1], n-1), a[-1])
    else:
        return solve(a[:-1], n-1)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        result = solve(a, n)
        print(result)

"""
This was coded after seeing the editorial.
But still the logic of calculating x is incorrect.

Needs more understanding for DP and this specific problem to solve this fully
"""