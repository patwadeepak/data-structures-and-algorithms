from typing import List
import heapq

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ps = [0]*n
        ps[0] = nums[0]
        for i in range(1, n):
            ps[i] = nums[i] + ps[i-1]
        
        h = []
        l = 0
        r = 0
        min_len = n+1
        heapq.heappush(h, (0, -1))
        for r in range(n):
            psl_1 = (0,0)
            if h:
                psl_1 = heapq.heappop(h)
                s = ps[r] - psl_1[0]
            else:
                s = ps[r]
                heapq.heappush(h, (nums[r], r))
            if s >= k:
                min_len = min(min_len, r-psl_1[1]+1)
        
        return -1 if min_len == n+1 else min_len

if __name__=='__main__':
    s = Solution()
    ans = s.shortestSubarray([1], 1)
    print(ans)

"""
Not Solved fully yet. Will Come Back to this.
"""
