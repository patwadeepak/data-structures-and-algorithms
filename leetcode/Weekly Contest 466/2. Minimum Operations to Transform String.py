# 3675. Minimum Operations to Transform String

from collections import Counter
class Solution:
    def minOperations(self, s: str) -> int:
        chars = 'abcdefghijklmnopqrstuvwxyz'

        counter = Counter(s)

        ops = 0
        for i, char in enumerate(chars[1:], start=1):
            if counter[char] != 0:
                ops += 1
                if i == 25:
                    break
                counter[chars[ord(char)+1 - ord('a')]] += 1

        return ops
