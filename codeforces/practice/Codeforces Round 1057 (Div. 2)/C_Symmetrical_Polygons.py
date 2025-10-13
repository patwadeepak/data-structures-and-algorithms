from collections import Counter
import heapq

def solve(n, a):
    longestSides = []
    ans = 0
    f = Counter(a)
    for ai in f.keys():
        if f[ai]%2 == 0:
           ans += f[ai]*ai
        else:
            if f[ai] > 0:
                if len(longestSides) < 2:
                    heapq.heappush(longestSides, ai)
                else:
                    if ai > longestSides[0]:
                        heapq.heapreplace(longestSides, ai)
            if f[ai]-1 > 0:
                ans += (f[ai]-1)*ai
    l = heapq.nlargest(2, longestSides)
    l1 = 0
    l2 = 0
    if len(l) == 2:
        l2 = l[1]
    if len(l) >= 1:
        l1 = l[0]

    if len(l) == 2 and l1 >= ans+l2:
        print(0)
        return 
    
    if len(l) == 1 and l1 >= ans:
        print(0)
        return

    if ans == 0:
        print(0)
        return
    ans += sum(longestSides)
    print(ans)

if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        a = list(map(int, input().split()))
        solve(n, a)

"""
This solution gives WA but core logic seems super solid.
Some minor mistake could be there or some edge case.
Will solve this later.
"""