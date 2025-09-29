# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

"""
It is just recursion and I realized it is just
fibonacci series with minor change on initial values
and essentially shifting fib one step to left.
Instead of fib(0) = 0, here we have dp(0) = 1.

At the same time, this is also the very starting
of bottom up tabulation approach for dynamic programming.
"""
