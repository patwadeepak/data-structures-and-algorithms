class Solution:
    def smallestNumber(self, n: int) -> int:
        binary = bin(n)
        a = "1"*(len(binary)-2)
        return int(a, 2)
