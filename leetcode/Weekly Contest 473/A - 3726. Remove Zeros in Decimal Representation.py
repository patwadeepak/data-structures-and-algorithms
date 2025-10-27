class Solution:
    def removeZeros(self, n: int) -> int:
        arr = []
        for ch in str(n):
            if ch != '0':
                arr.append(ch)

        return int(''.join(arr))