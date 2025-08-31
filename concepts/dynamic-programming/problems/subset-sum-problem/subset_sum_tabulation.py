class Solution:
    def isSubsetSum (self, arr, sum):
        self.arr = arr
        self.cache = [[False]*(sum+1) for _ in range(len(arr)+1)]
        return self.isSubsetSumTabulation(len(arr), sum)

    def isSubsetSumTabulation (self, n, sum):
        for i in range(1, n+1):
            for j in range(1, sum+1):
                if sum-self.arr[i-1] > 0:
                    self.cache[i][j] = self.cache[i-1][sum-self.arr[i-1]] or self.cache[i-1][sum]
                else:
                    self.cache[i][j] = self.cache[i-1][sum]

        return self.cache[n][sum]


if __name__ == '__main__':
    s = Solution()

    arr = [3, 34, 4, 12, 5, 2]
    sum = 30
    r = s.isSubsetSum(arr, sum)
    print(r) # False

    arr = [3, 34, 4, 12, 5, 2]
    sum = 9
    r = s.isSubsetSum(arr, sum)
    print(r) # True

"""
This code may or may not be correct.
I have not submitted or tested this one yet.
"""