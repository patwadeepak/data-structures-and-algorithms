# https://neetcode.io/problems/permutation-string?list=neetcode150

"""
My very own solution.
Seems too complicated. There must be a better solution.
"""
from collections import Counter

class Solution:
    def checkPossibility(self, c1: dict, c2: dict):
        for k1, v1 in c1.items():
            if k1 not in c2:
                return False
            elif c2[k1] < v1:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter(s2)

        if not self.checkPossibility(c1, c2):
            return False
        
        is_p = False

        n = len(s2)
        l = 0
        r = n-1

        while l <= r and r-l+1 >= len(s1):
            moved = False
            if s2[l] not in c1:
                l += 1
                moved = True
            if s2[r] not in c1:
                r -= 1
                moved = True
            
            if r-l+1 == len(s1):
                is_p = self.checkPossibility(c1, c2)
                if not is_p:
                    break
                

            if not moved:
                if l+len(s1) <= len(s2) and self.checkPossibility(c1, Counter(s2[l:l+len(s1)])):
                    is_p = True
                    break
                else:
                    c2[s2[l]] -= 1
                    l += 1
                
                if r-l+1 == len(s1):
                    is_p = self.checkPossibility(c1, c2)
                    if not is_p:
                        break
                
                if r-len(s1)+1 >= 0 and self.checkPossibility(c1, Counter(s2[r-len(s1)+1:r+1])):
                    is_p = True
                    break
                else:
                    c2[s2[r]] -= 1
                    r -= 1

                if r-l+1 == len(s1):
                    is_p = self.checkPossibility(c1, c2)
                    if not is_p:
                        break

        return is_p

if __name__ == "__main__":
    s = Solution()

    s1="abc"
    s2="lecaabee"
    output = s.checkInclusion(s1, s2)
    print(output)