class Solution:
    def isSubsetSum (self, arr, sum):
        if sum == 0:
            return True
        if sum < 0 or not arr:
            return False

        return self.isSubsetSum(arr[:-1], sum-arr[-1])\
            or self.isSubsetSum(arr[:-1], sum)


if __name__ == '__main__':
    s = Solution()

    arr = [3, 34, 4, 12, 5, 2]
    sum = 30
    r = s.isSubsetSum(arr, sum)
    print(r) # answer - False

    arr = [3, 34, 4, 12, 5, 2]
    sum = 9
    r = s.isSubsetSum(arr, sum)
    print(r) # True
