# https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1
class Solution:
    def knapsack(self, W, val, wt):
        self.val = val
        self.wt = wt
        self.d = [[-1]*(W+1) for _ in range(len(val)+1)]

        self.d[0] = [0]*len(self.d[0])
        for item in self.d:
            item[0] = 0

        return self.solve(W, len(val))

    def solve(self, W, i):
        for j in range(1, i+1):
            for w in range(1, W+1):
                pick = 0
                if w >= self.wt[j-1]:
                    pick = self.val[j-1] + self.d[j-1][w - self.wt[j-1]]
                not_pick = self.d[j-1][w]

                self.d[j][w] = max(pick, not_pick)

        return self.d[i][w]

if __name__ == '__main__':
    W = 4
    val = [1, 2, 3]
    wt = [4, 5, 1]

    s = Solution()
    r = s.knapsack(W, val, wt)
    print(r)
