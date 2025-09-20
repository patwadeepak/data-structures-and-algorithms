# https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode150

"""
Solution without division.
A simple introduction to prefix and suffix arrays.
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1]*len(nums), [1]*len(nums)
        for i, num in enumerate(nums):
            j = len(nums)-i-1

            if i-1 >= 0:
                prefix[i] = prefix[i-1]*nums[i-1]
            if j+1 <= len(nums)-1:
                suffix[j] = suffix[j+1]*nums[j+1]
        
        res = [p*s for p, s in zip(prefix, suffix)]

        return res