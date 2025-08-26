# Dynamic Programming
# Coins Change - Count Ways to make sum

# https://www.geeksforgeeks.org/problems/coin-change2448/1

def solve(a, n):
    if n < a[0]:
        return 0
    elif n == a[0]:
        return 1
    
    # write code dp logic here
    


if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        a.sort()
        solve(a, n)
