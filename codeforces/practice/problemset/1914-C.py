def recursion(k, n, used_i, a, b):
    if k == 0:
        return 0
    
    if n-1 < 0:
        return 0

    v1 = 0 
    v2 = 0
    if n-1 not in used_i:
        used_i.add(n-1)
        v1 = recursion(k-1, n-1, used_i, a, b) + a[n-1]
    else:
        v2 = recursion(k-1, n-1, used_i, a, b) + b[n-1]
    used_i.discard(n-1)
    v3 = recursion(k, n-1, used_i, a, b)

    return max(v1, v2, v3)
    

def solve(n, k, a, b):
    ans = recursion(k, n, set(), a, b)
    print(ans)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, k = list(map(int, input().split(' ')))
        a = list(map(int, input().split(' ')))
        b = list(map(int, input().split(' ')))
        solve(n, k, a, b)


"""
Turns out, I was trying to use DP when it
could be easily solved with greedy method.

Will Fix this later.
"""