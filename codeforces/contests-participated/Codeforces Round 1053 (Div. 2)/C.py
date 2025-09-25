def solve(a, n):
    d = [0]*(2*n-1)
    for i in range(len(a)):
        j = 2*n-i-1
        if j-1 >= 0:
            d[j-1] = a[j] - a[j-1]
    
    k = [0]*n

    for i in range(n):
        k[i] = sum(a[2*n-i:]) - sum(a[:i]) + sum(d[i:2*n-i-1:2])
    
    print(*k)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        solve(a, n)

"""
This is giving correct results and I think it is correct solution.
But the line 11 where we add three sums, ends up being very slow and throws TLE.

I just need to create a sum out of loop and change it incrementally
to get all three terms to keep things linear and avoid TLE.

Did not had enough time to make this improvement in contest.
"""
