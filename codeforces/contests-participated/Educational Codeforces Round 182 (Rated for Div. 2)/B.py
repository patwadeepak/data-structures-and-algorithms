def solve(a, n):
    if n <= 1:
        return 0

    multi_zeros = False
    zero_count = 0
    for num in a:
        if num == 0:
            zero_count += 1
            if zero_count > 1:
                multi_zeros = True
                break
    
    l = 0
    r = n-1

    while l <= r:
        if a[l] == l+1:
            l += 1
        elif a[l] == 0:
            if multi_zeros:
                break
            else:
                pass
                
#  or (a[l] == 0 and not multi_zeros):
    while l <= r and r >= 0:
        if a[r] == r+1 or (a[r] == 0 and not multi_zeros):
            r -= 1
        else:
            break 
    
    return max(r - l + 1, 0)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        op = solve(a, n)
        print(op)

"""
WIP
"""