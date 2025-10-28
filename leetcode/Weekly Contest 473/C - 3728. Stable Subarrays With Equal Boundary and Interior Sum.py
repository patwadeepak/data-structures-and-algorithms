from typing import List
from collections import defaultdict as dd, deque

class Solution:
    def countStableSubarrays(self, a: List[int]) -> int:
        n = len(a)
        ps = [0]*n
        ps[0] = a[0]
        for i in range(1, n):
            ps[i] = ps[i-1] + a[i]

        # ps[i] = ps[i-1] + a[i]
        # ps[r-1] - ps[l] = a[l] = a[r]
        # ps[r] - a[r] - ps[l] = a[l] = a[r]
        # ps[r] - a[r] = a[l] + ps[l]
        # ps[r] = ps[l] + 2*v
        # v = a[r] = a[l]
        s = dd(int)
        q = deque([])
        stable = 0
        for i in range(n):
            if (ps[i], a[i]) in s:
                stable += s[(ps[i], a[i])]
            
            q.append((ps[i]+2*a[i],a[i]))
            if len(q) >= 2:
                x, y = q.popleft()
                s[(x,y)] += 1

        return stable