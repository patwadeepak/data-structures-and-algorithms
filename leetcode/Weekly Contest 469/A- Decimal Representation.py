from typing import List

class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        a = []
        multiple = 0
        while n > 0:
            digit = n%10
            if digit != 0:
                a.append(10**(multiple)*digit)
            n = n//10
            multiple += 1

        return a[::-1]