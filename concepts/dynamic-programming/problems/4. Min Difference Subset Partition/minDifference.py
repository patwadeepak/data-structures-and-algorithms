# https://www.geeksforgeeks.org/problems/minimum-sum-partition3317/1

class Solution:
    def minDifference(self, nums):
        sums = set([0])
        
        for num in nums:
            list_sums = list(sums)
            for s in list_sums:
                sums.add(s+num)

        t = sum(nums)
        diff = float('inf')
        for s in sums:
            diff = min(diff, abs(t - 2*s))
        return diff

if __name__=='__main__':
    b = Solution()

    arr = list(map(int, '3 9 8 10 6 3 3 8 6 6 10 9 9 7 3 10'.split(' ')))
    print('correct: ', 0, '\nOutput: ', b.minDifference(arr), '\n')

    arr = [3,9,7,3]
    print('correct: ', 2, '\nOutput: ', b.minDifference(arr), '\n')

"""
This solution is better than all solutions mentioned in the editorial.
Took some time to think about this but it was worth it.
"""
