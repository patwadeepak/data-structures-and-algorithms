class Solution:
    def isSubsetSum (self, arr, sum):
        dp = [[None]*(sum+1) for _ in range(len(arr)+1)]
        dp[0] = [False]*(sum+1)

        # base case initialization
        for i in range(len(arr)+1):
            dp[i][0] = True

        # filling up the dp table
        for i in range(1, len(arr)+1):
            for j in range(1, sum+1):
                if j-arr[i-1] >= 0:
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[len(arr)][sum]


if __name__ == '__main__':
    s = Solution()

    # arr = [3, 34, 4, 12, 5, 2]
    # sum = 30
    # r = s.isSubsetSum(arr, sum)
    # print(r) # False

    arr = [3, 34, 4, 12, 5, 2]
    sum = 9
    r = s.isSubsetSum(arr, sum)
    print(r) # True
