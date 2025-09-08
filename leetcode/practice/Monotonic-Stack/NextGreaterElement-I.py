# 496. Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/description/

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        s = []
        for i in range(len(nums2)):
            while s and s[-1] < nums2[i]:
                a = s.pop()
                d[a] = nums2[i]
            s.append(nums2[i])
        
        return [d.get(x, -1) for x in nums1]
            
