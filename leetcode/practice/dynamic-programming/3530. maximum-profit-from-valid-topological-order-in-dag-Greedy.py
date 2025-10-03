from collections import defaultdict
from typing import List

class Solution:
    def explore(self):
        while self.q:
            min_score = float('inf')
            mutliplier = len(self.output)+1
            picked_pair = None
            for score, node in self.q:
                new_score = mutliplier*score
                if mutliplier*score < min_score:
                    min_score = new_score
                    picked_pair = (score, node)

            s, node = picked_pair
            self.output.append((s, node))
            self.q.discard(picked_pair)
            for child in self.g[node]:
                self.indegree[child] -= 1
                if self.indegree[child] == 0:
                    self.q.add((self.score[child], child))

    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        self.g = defaultdict(list)
        self.score = score
        self.indegree = [0]*n
        self.n = n
        self.output = []
        self.q = set()

        for u,v in edges:
            self.g[u].append(v)
            self.indegree[v] += 1
        
        for i in range(n):
            if self.indegree[i] == 0:
                self.q.add((self.score[i], i))

        self.explore()

        return sum([x * i for i, (x, _) in enumerate(self.output, start=1)])

if __name__=='__main__':
    s = Solution()

    """
    score - 77 89 1 2 40 22 10
    arr   - 0  1  2 3  4  5  6

          3
        /   \
      0       6
    / \      / \
   1   2    /   4
        \ /
         5
    """
    # n = 7
    # edges = [
    #     [3, 0],
    #     [3, 6],
    #     [0, 1],
    #     [0, 2],
    #     [6, 4],
    #     [6, 5],
    #     [2, 5],
    # ]
    # score = [77, 89, 1, 2, 40, 22, 10]

    n = 5
    edges = [[1,2],[0,3],[1,4],[2,3],[1,3]]
    score = [50913,47946,97391,27488,69147]

    """
0     1
|   / | \
|  /  2  4
| / /
3  
"""

    profit = s.maxProfit(n, edges, score)

    print(profit)

"""
This Greedy approach is actually not the correct solution.
But I have still learnt a lot about Kahn's algorithm
and topological sort and the implementation.
So, keeping this here.

Original Kahn's Algo uses a queue instead of a set.
And all the code from line 7 to 14 is not there.
Just a queue.popleft() instead.
"""
