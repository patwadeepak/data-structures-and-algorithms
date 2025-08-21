# C1. The Cunning Seller (easy version)

import math

def solve(n):
    x = math.ceil(math.log(n, 3))

    cost = (3**(x+1)) + (x*(3**(x-1)))

    print(int(cost))

if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n = int(input())

        solve(n)

# Incorrect