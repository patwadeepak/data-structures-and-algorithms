# 3698. Split Array With Minimum Difference
# https://leetcode.com/problems/split-array-with-minimum-difference/

from typing import List

class Solution:
    def splitArray(self, nums: List[int]) -> int:
        prefix_sum = [0]*len(nums)
        prefix_sum[0] = nums[0]
        peak = None
        found = False
        cutoff = None
        inc = True
        dec = True
        for i, num in enumerate(nums[1:], start=1):
            prefix_sum[i] = prefix_sum[i-1] + num
            if nums[i-1] >= num:
                inc = False
            if nums[i-1] <= num:
                dec = False
            if not found:
                if nums[i-1] > num:
                    found = True
                    peak = i-1
                elif nums[i-1] == num:
                    found = True
                    cutoff = i
            else:
                if nums[i-1] <= num:
                    return -1

        if not found:
            if dec:
                peak = 0
            elif inc:
                peak = len(nums) - 1

        if peak is not None and cutoff is None:
            a = prefix_sum[peak-1] if peak-1 >= 0 else 0
            b = prefix_sum[-1] - prefix_sum[peak]
            return min(abs(a-b+nums[peak]), abs(a-b-nums[peak]))
        elif cutoff is not None:
            a = prefix_sum[-1] - prefix_sum[cutoff-1]
            b = prefix_sum[cutoff-1]
            return abs(a-b)

        return -1

"""
Solved After Contest
"""
