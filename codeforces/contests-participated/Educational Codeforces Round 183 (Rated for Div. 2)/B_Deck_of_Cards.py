from collections import Counter

def solve(n, k, s):
    if k == n:
        return '-'*n

    c = Counter(s)
    start = c['0']*'-'
    end = c['1']*'-'
    mid_start = c['2']*'?'

    plus = n - len(mid_start)*2 - len(start) - len(end)
    pluses = '+'*plus

    if plus < 0:
        return start + (mid_start*2)[:plus] + end

    return start + mid_start + pluses + mid_start + end

if __name__=='__main__':
    t = int(input())

    for i in range(t):
        n, k = map(int, input().split())
        s = input()
        print(solve(n, k, s))