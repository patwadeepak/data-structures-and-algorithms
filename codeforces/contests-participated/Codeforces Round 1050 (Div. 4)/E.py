from collections import Counter

def solve(n, k, a):
    if n%k != 0:
        return 0
    
    c = Counter(a)

    for k, v in c.items():
        if v%k == 0:
            pass
        else:
            return 0
    
    ans = 0
    for window in range(1, n+1):
        value =  n - window
        ans += value
    
    return ans

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, k = list(map(int, input().split(' ')))
        a = list(map(int, input().split(' ')))
        print(solve(n, k, a))

"""
Did not solve this fully
"""
