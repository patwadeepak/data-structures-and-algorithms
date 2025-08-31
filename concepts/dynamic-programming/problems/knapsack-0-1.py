# https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1
class Solution:
    def knapsack(self, W, val, wt):
        self.val = val
        self.wt = wt
        self.d = [[-1]*(W+1) for _ in range(len(val)+1)]
        
        return self.solve(W, len(val))

    def solve(self, W, i):
        if W <= 0 or i <= 0:
            return 0

        c = self.d[i][W]
        if c != -1:
            return c

        pick = 0
        if W >= self.wt[i-1]:
            pick = self.val[i-1] + self.solve(W - self.wt[i-1], i-1)
        not_pick = self.solve(W, i-1)

        self.d[i][W] = max(pick, not_pick)

        return self.d[i][W]

if __name__ == '__main__':
    W = 4
    val = [1, 2, 3]
    wt = [4, 5, 1]

    s = Solution()
    r = s.knapsack(W, val, wt)
    print(r)
