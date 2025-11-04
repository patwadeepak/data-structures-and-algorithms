from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        nse = [-1]*n # next smaller element's index array
        s = []
        for i in range(n):
            while s and heights[s[-1]] > heights[i]:
                v = s.pop()
                nse[v] = i
            s.append(i)
        
        pse = [-1]*n # previous smaller element's index array
        s = []
        for i in range(n-1, -1, -1):
            while s and heights[s[-1]] > heights[i]:
                v = s.pop()
                pse[v] = i
            s.append(i)

        maxA = 0
        for i in range(n):
            r = nse[i]-1 if nse[i] != -1 else n-1
            l = pse[i]+1 if pse[i] != -1 else 0

            w = r-l+1
            maxA = max(maxA, w*heights[i])
        
        return maxA

if __name__ == '__main__':
    s = Solution()
    ans = s.largestRectangleArea([2, 1, 5, 6, 2, 3])
    print(ans)

"""
My very own solution.
This can obviously be optimised.
"""