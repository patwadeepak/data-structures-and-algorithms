class Solution:
    def lexSmallest(self, s: str) -> str:
        smallest = s
        for i in range(len(s)):
            new_str = s[0:i][::-1]+s[i:]
            if smallest > new_str:
                smallest = new_str

            new_str = s[0:i]+s[i:][::-1]
            if smallest > new_str:
                smallest = new_str

        return smallest