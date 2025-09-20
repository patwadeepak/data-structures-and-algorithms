# https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode150

"""
With division.
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        zeros = 0
        for num in nums:
            if num != 0:
                p *= num
            else:
                zeros += 1

        if zeros > 1:
            return [0]*len(nums)
                
        res = []
        for num in nums:
            if zeros == 1:
                if num != 0:
                    res.append(0)
                else:
                    res.append(p)
            elif num != 0:
                res.append(p//num)
            else:
                res.append(p)
        
        return res