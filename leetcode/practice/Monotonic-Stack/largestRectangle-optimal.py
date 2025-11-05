from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        s = []
        max_area = 0

        for i in range(n+1):
            while s and (i==n or heights[s[-1]] >= heights[i]):
                h = heights[s.pop()]
                w = i if not s else i - s[-1] - 1
                max_area = max(max_area, w*h)
            s.append(i)

        return max_area

"""
for i in range(n+1):
the n+1 trick is called sentinel, it is often used to optimize a loops.
for example a grid representing a forest. Each cell can be a tree or path.
to not check grid boundary everywhere. we add 1 layer thick trees around the grid
and let the trees itself become the boundary. this trick simplifies code.

similarly, here we have assumed that there is a zero height bar at the end.
this forces loop to run one extra time and all the bars that were not processed
after looping n times, will now be processed since all provided bars cannot
extend after zero bar for sure. to make this work we put i==n in the while 
condition as well.

Also, notice how in the standard solution we use heights[s[-1]] > heights[i]
but here we are using >= , this is because the idea of solution itself
has been modified a little here.
We are using a monotonic stack, and even after we pop once, we look again
at the stack in line w = i if not s else i-s[-1]-1, here s[-1], is the 
bar that is strictly smaller than the one we just popped to process.
"""