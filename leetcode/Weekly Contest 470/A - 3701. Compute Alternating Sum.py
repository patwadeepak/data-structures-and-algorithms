from typing import List

class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        m = True
        s = 0
        for num in nums:
            s += num*(1 if m else -1)
            m = not m
        return s