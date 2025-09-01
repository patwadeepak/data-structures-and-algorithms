# https://www.geeksforgeeks.org/problems/subset-sum-problem2014/1

class Solution:
    def equalPartition(self, arr):
        s = sum(arr)
        if s%2 != 0:
            return False

        s = s//2

        n = len(arr)

        dpi_1 = [False]*(s+1)
        dpi   = [False]*(s+1)

        dpi_1[0] = True
        dpi[0] = True

        for i in range(1, n+1):
            for j in range(1, s+1):
                if j-arr[i-1] >= 0:
                    dpi[j] = dpi_1[j-arr[i-1]] or dpi_1[j]
                else:
                    dpi[j] = dpi_1[j]

            dpi_1 = dpi
            dpi = [False]*(s+1)
            dpi[0] = True

        return dpi_1[s]

if __name__=='__main__':
    s = Solution()

    arr = [1, 5, 11, 5]
    print(s.equalPartition(arr))

"""
Writing a Space optimized tabulation DP seems like the best possible solution.
But honestly I would only do this if I am running out of memory
because the added effort seems not worth it.

Having said that if I have enough practice then it might become effortless. :)
"""
