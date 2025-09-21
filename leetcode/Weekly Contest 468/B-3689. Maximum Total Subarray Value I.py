from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maxx = float('-inf')
        minn = float('inf')

        for num in nums:
            maxx = max(maxx, num)
            minn = min(minn, num)

        return (maxx - minn) * k