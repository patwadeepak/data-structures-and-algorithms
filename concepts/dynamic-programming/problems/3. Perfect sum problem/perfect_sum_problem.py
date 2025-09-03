# Perfect Sum Problem
# https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1

# Space Optimized DP solution :)

class Solution:
    def perfectSum(self, arr, target):
        dpi_1 = [0 for _ in range(target+1)]
        dpi_1[0] = 1

        dpi = [0 for _ in range(target+1)]
        dpi[0] = 1

        for i in range(1, len(arr)+1):
            for j in range(target+1):
                if j >= arr[i-1]:
                    dpi[j] = dpi_1[j-arr[i-1]] + dpi_1[j]
                else:
                    dpi[j] = dpi_1[j]
            
            dpi_1 = dpi
            dpi = dpi = [0 for _ in range(target+1)]
            dpi[0] = 1

        return dpi_1[target]

if __name__=='__main__':
    s = Solution()

    arr = [0,1]
    target = 1
    print('correct: ', 2, '\nOutput: ', s.perfectSum(arr, target), '\n')

    arr = [5, 2, 3, 10, 6, 8]
    target = 10
    print('correct: ', 3, '\nOutput: ', s.perfectSum(arr, target), '\n')

    arr = [2, 5, 1, 4, 3]
    target = 10
    print('correct: ', 3, '\nOutput: ', s.perfectSum(arr, target), '\n')

    arr = [5, 7, 8]
    target = 3
    print('correct: ', 0, '\nOutput: ', s.perfectSum(arr, target), '\n')

    arr = [25, 2, 88, 22]
    target = 0
    print('correct: ', 1, '\nOutput: ', s.perfectSum(arr, target), '\n')

