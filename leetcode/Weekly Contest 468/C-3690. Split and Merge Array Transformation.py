from typing import List

class Solution:
    def bfs(self, q, nums2, count):
        nums1 = q.pop()
        for l in range(6):
            for r in range(l+1, 6):
                if r-l <= 0:
                    continue
                before = nums1[0:l]
                after = nums1[r:]
                if len(before) > 0:
                    for i, item in enumerate(before):
                        x = list(before[0:i])
                        x.extend(nums1[l:r])
                        x.extend(before[i:])
                        x.extend(after)
                        x = tuple(x)
                        if x == tuple(nums2):
                            return count, True
                        if x != tuple(nums1):
                            q.add(x)
                if len(after) > 0:
                    for i, item in enumerate(after):
                        x = list(before[:])
                        x.extend(after[0:i+1])
                        x.extend(nums1[l:r])
                        x.extend(after[i+1:])
                        x = tuple(x)
                        if x == tuple(nums2):
                            return count, True
                        if x != tuple(nums1):
                            q.add(x)
        count += 1
        while len(q) > 0:
            count, found = self.bfs(q, nums2, count)
            if found:
                return count, True

    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        if tuple(nums1) == tuple(nums2):
            return 0
        
        d = {}
        for i, num in enumerate(nums1):
            if num not in d:
                d[num] = i
        
        for i, (num1, num2) in enumerate(zip(nums1, nums2)):
            nums1[i] = d[num1]
            nums2[i] = d[num2]

        count,_ = self.bfs({tuple(nums1)}, nums2, 0)
        print(count)

                    
if __name__=='__main__':
    s = Solution()

    s.minSplitMerge([1,1,2,3,4,5], [5,4,3,2,1,1])

"""
Ugly attempt at a solution.
Not a solution.
"""