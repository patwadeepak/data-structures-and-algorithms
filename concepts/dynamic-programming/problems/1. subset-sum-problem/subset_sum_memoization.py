class Solution:
    def isSubsetSum (self, arr, sum):
        self.arr = arr
        self.cache = {}
        return self.isSubsetSumRec(len(arr), sum)


    def isSubsetSumRec (self, n, sum):
        if sum == 0:
            return True
        if sum < 0 or n < 0:
            return False

        c = self.cache.get((n, sum))
        if c is not None:
            return c

        res = self.isSubsetSumRec(n-1, sum)
        # missed the n-1 >= 0 check and spent quite some time here to figure this out.
        # python can have negative index so this was not even throwing error :p
        if n-1 >= 0 and self.arr[n-1] <= sum:
            res = res or self.isSubsetSumRec(n-1, sum-self.arr[n-1])

        self.cache[(n, sum)] = res

        return res


if __name__ == '__main__':
    s = Solution()

    arr = [6, 6, 6, 3, 8]
    sum = 16
    r, cache = s.isSubsetSum(arr, sum)
    print(r) # True

    # arr = [3, 34, 4, 12, 5, 2]
    # sum = 30
    # r = s.isSubsetSum(arr, sum)
    # print(r) # False

    # arr = [3, 34, 4, 12, 5, 2]
    # sum = 9
    # r = s.isSubsetSum(arr, sum)
    # print(r) # True
