from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        last = nums2[-1]
        min_diff = float('inf')

        is_found_in_middle = False

        ops = 0
        for i, num in enumerate(nums1):
            ops += abs(num-nums2[i])
            if num >= nums2[i] and nums2[i] <= last <= num:
                is_found_in_middle = True
            elif num <= nums2[i] and num <= last <= nums2[i]:
                is_found_in_middle = True

            min_diff = min(min_diff, abs(last-num), abs(last-nums2[i]))

        if is_found_in_middle:
            ops += 1
        else:
            ops += min_diff + 1

        return ops
