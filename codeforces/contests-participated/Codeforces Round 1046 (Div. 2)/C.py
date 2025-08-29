# C. Against the Difference

def is_block(x):
    return x == [len(x)]*x

def solve(a, n):
    if is_block(a):
        print(len(a))
        return
    
    d = {}
    for i in range(1, n+1):
        if a[i] in d:
            d[a[i]].append(i)
        else:
            d[a[i]] = [i]
    
    keys = list(d.keys())
    keys.sort()
    
    blocks = []

    for k in keys:
        i_arr = d[k]
        if len(i_arr) < k:
            pass
        else:
            n_blocks = len(i_arr) // k
            # maxx = max(maxx, n_blocks*k)
            if n_blocks == 1:
                blocks = [i_arr[:k], i_arr[k:2*k]]
            


if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        solve(a, n)

"""
Need more DP muscles before I can tackle these in contests.
Not A Solution.
"""