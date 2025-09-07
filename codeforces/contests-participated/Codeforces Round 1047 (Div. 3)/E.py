# E. Mexification

def solve(n, k, a):
    s = set(a)

    mex = None
    for num in range(n+1):
        if num not in s:
            mex = num
            break
    
    less_sum = 0
    count_more = 0

    for num in a:
        if num < mex:
            less_sum += num
        else:
            count_more += 1

    if n == 2 and 0 in s and 2 in s:
        print(1)
        return
    
    if k%2 == 0:
        print(count_more*(mex+1) + less_sum)
    else:
        print(count_more*mex + less_sum)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, k = list(map(int, input().split(' ')))
        a = list(map(int, input().split(' ')))
        solve(n, k, a)
