def solve(n, rk, ck, rd, cd):
    ans = 0
    if rk > rd:
        ans = max(ans, n - rd)
    if rk < rd:
        ans = max(ans, rd)
    
    if ck > cd:
        ans = max(ans, n - cd)
    if ck < cd:
        ans = max(ans, cd)

    return ans

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, rk, ck, rd, cd = list(map(int, input().split()))
        print(solve(n, rk, ck, rd, cd))

"""
Solved After contest
"""