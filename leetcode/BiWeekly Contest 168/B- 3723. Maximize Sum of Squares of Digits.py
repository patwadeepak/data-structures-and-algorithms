class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        num_str = []
        for i in range(num):
            if sum >= 9:
                num_str.append('9')
                sum -= 9
            elif sum > 0:
                num_str.append(str(sum))
                sum = 0
            else:
                num_str.append('0')

        return ''.join(num_str) if sum == 0 else ''
