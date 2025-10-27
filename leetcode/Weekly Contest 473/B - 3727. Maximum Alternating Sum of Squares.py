from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: abs(x))
        k = len(nums)//2

        score = 0
        for i in nums[:k]:
            score -= i*i

        for i in nums[k:]:
            score += i*i

        return score
        