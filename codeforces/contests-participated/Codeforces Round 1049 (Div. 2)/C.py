def solve(a, n):
    fa = 0
    minn = float('-inf')
    maxx = float('-inf')
    for i, num in enumerate(a):
        if i%2 == 0:
            m = 1
        else:
            m = -1
        fa += m*num
        maxx = max(maxx, 2*num-i)
        minn = max(minn, 2*m*num+i)

    cost = maxx - minn
    if cost > 0:
        print(fa + cost)
    else:
        print(fa)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        solve(a, n)

"""
Could not solve this one in contest.
I figured out everything except the last if else detail
for 2 cases of possible swap.

Figuring out that Bob will always choose to end the game in 
his very first chance was amazing and exciting.
"""