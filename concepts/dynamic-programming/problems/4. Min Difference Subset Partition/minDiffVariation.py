# https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/description/

class Solution:
    def rec(self, arr, target, s):
        print('arr: ', arr, ' target: ', target, ' s: ', s)
        if (target, s) in self.memo:
            return

        if target == 0:
            self.minDiff = min(abs(self.total - 2*s), self.minDiff)
            self.memo.add((target, s))
            return

        if len(arr) < target:
            self.memo.add((target, s))
            return
        if not arr:
            self.memo.add((target, s))
            return
        
        if target >= 0:
            self.rec(arr[:-1], target-1, s+arr[-1])
        
        self.rec(arr[:-1], target, s)
        self.memo.add((target, s))


    def minimumDifference(self, nums):
        self.minDiff = float('inf')
        self.nb2 = len(nums)//2
        self.total = sum(nums)
        self.memo = set()
        self.rec(nums, self.nb2, 0)


        return self.minDiff

if __name__=='__main__':
    b = Solution()

    # failing_test_case = [7772197,4460211,-7641449,-8856364,546755,-3673029,527497,-9392076,3130315,-5309187,-4781283,5919119,3093450,1132720,6380128,-3954678,-1651499,-7944388,-3056827,1610628,7711173,6595873,302974,7656726,-2572679,0,2121026,-5743797,-8897395,-9699694]
    # print('correct: ', 72, '\nOutput: ', b.minimumDifference(failing_test_case), '\n')

    arr = list(map(int, '-36 36'.split(' ')))
    print('correct: ', 72, '\nOutput: ', b.minimumDifference(arr), '\n')

    arr = [3,9,7,3]
    print('correct: ', 2, '\nOutput: ', b.minimumDifference(arr), '\n')

    arr = [2, -1, 0, 4, -2, -9]
    print('correct: ', 0, '\nOutput: ', b.minimumDifference(arr), '\n')

"""
Not solved fully. This is a Knapsack variation but quite hard for now.
"""