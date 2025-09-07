# 3676. Count Bowl Subarrays

class Solution:
    def bowlSubarrays(self, nums):
        self.sarr = 0
        self.nums = nums
        self.memo = set()
        self.solve(0, len(nums)-1)
        return self.sarr
    
    def solve(self, l, r):
        if (l,r) in self.memo:
            return
        if r - l + 1 < 3:
            self.memo.add((l,r))
            return
        
        if max(self.nums[l+1:r]) < min(self.nums[l], self.nums[r]):
            self.sarr += 1

        self.solve(l+1,r)
        self.solve(l,r-1)
        self.memo.add((l,r))

"This is TLE"
