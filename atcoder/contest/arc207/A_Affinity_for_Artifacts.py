from math import factorial

N = 998244353

def solve(a, n, x):
    dp = [[0]*(x+1) for _ in range(n+1)]

    for i in range(1, n+1):
        zero = 0
        for num in a[:i]:
            if num == 0:
                zero += 1
        dp[i][0] = factorial(zero)%N
    
    for i in range(1, n+1):
        for j in range(1, x+1):
            dp[i][j] += dp[i-1][j]
            if j-a[i-1] >= 0:
                dp[i][j] += dp[i][j-a[i-1]]
            

    

if __name__ == '__main__':
    n, x = list(map(int, input().split()))
    a = map(int, input().split())
    print(solve(a, n, x))

"""
Grass is always greener on the other side.
I was just trying to peek into the contests meant for div 1.
To get a feel of how tough/good problems they have.
I was not disappointed. This very first problem looks like
a very nice problem and probably a DP problem with enough
twists that I can't solve it now. But it sure seems awesome. :)
"""