from typing import List
from collections import Counter

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        f = Counter(nums)
        ans = 0
        for v in list(f.keys()):
            if f[v]%k == 0:
                ans += v*f[v]

        return ans
        