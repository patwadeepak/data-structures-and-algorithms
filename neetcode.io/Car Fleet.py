from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        comb = [[x, y] for x,y in sorted(zip(position, speed), reverse=True)]

        fleets = len(position)
        while comb[-1][0] < target:
            for i, (p,s) in enumerate(comb):
                last = None if i == 0 else comb[i-1][0]
                if p < target:
                    comb[i][0] += s
                    if last is not None and comb[i][0] >= last:
                        fleets -= 1
                        last = min(comb[i][0], last)
                    if last is None:
                        last = comb[i][0]
        
        return fleets

if __name__=='__main__':
    s = Solution()

    result = s.carFleet(10, [4,1,0,7], [2,2,1,1])
    print(result)
'''
7, 2 -> 10-7 = 3/2 = 1.5
5, 4 -> 10-5 = 5/4 = 1.25
3, 1 -> 10-3 = 7/1 = 7
0, 3 -> 10-0 = 10/3 = 3.33


Attempt later again.
'''