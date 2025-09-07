# https://codeforces.com/contest/2137/problem/C
# C. Maximum Even Sum

import math

def solve(a, b):
    if b == 1 and a%2 != 0:
        print(int(a+b))
        return
    elif b == 1:
        print(-1)
        return

    found = False
    k = 2 
    while k <= math.ceil(math.sqrt(b)):
        if b%k == 0:
            found = True
            break
        k += 1
    
    if not found:
        if a%2 != 0:
            print(int(a*b) + 1)
        else:
            print(-1)
    else:
        m = b/k
        x = a*m + k
        if x%2 == 0:
            print(int(x))
        else:
            print(-1)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        a, b = list(map(int, input().split(' ')))
        solve(a, b)
