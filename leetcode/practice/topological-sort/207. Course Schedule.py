# https://leetcode.com/problems/course-schedule/description/
from typing import List

class Solution:
    def explore(self, g, vis, s, node, op):
        if vis[node] is None:
            if node in s:
                return True
            return
        elif vis[node]:
            return

        s.append(node)
        vis[node] = None
        keys = g.get(node, [])
        for key in keys:
            cycle = self.explore(g, vis, s, key, op)
            if cycle:
                return True
        item = s.pop()
        vis[item] = True
        op.append(item)

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        s = []
        g = {}
        for u, v in prerequisites:
            arr = g.get(v, [])
            arr.append(u)
            g[v] = arr
        
        vis = [False]*numCourses

        op = []

        for key in g.keys():
            cycle = self.explore(g, vis, s, key, op)
            if cycle:
                return False
        return True

if __name__ == '__main__':
    s = Solution()

    output = s.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]])
    print(output)

"""
Faced a topological sort question in yesterday's div2 codeforces.
On studying it, I figured it was easy enough that I could have solved it 
only if I knew topological sort. So, Solving relevant questions now.

This is a direct use of that, although we don't output the topologically
sorted array of courses to take in order to complete all of them but I still
calculate and keep them for practice in op list.
"""
