from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while s and temperatures[s[-1]] < t:
                ti = s.pop()
                res[ti] = (i - ti)
            s.append(i)

        return res
