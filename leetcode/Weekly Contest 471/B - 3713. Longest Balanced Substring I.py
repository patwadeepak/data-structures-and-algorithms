from copy import deepcopy
class Solution:
    def check(self, a):
        value = None
        for ai in a:
            if ai != 0:
                if value is None:
                    value = ai
                elif ai != value:
                    return False
        return True

    def longestBalanced(self, s: str) -> int:
        a = [0]*26
        for ch in s:
            a[ord(ch)-ord('a')] += 1

        if self.check(a):
            return len(s)

        for w in range(len(s)-1, 0, -1):
            a[ord(s[w])-ord('a')] -= 1
            b = deepcopy(a)
            for start in range(0, len(s)-w+1):
                if self.check(b):
                    return w
                b[ord(s[start])-ord('a')] -= 1
                b[ord(s[w])-ord('a')] += 1

if __name__=="__main__":
    s = Solution()

    print(s.longestBalanced('zzabccy'))

"""
This one was an attempt in contest. WA
"""