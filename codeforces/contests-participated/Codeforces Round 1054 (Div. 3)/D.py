def solve(arr, n):
    if n <= 3:
        print(0)
        return
    a, b = 0, 0
    ac, bc = 0, 0
    for i, ai in enumerate(arr):
        if ai == 'a':
            a += i
            ac += 1
        else:
            b += i
            bc += 1
    
    ai_avg = a//ac
    bi_avg = b//bc

    # bring all a to center
    # find nearest a
    i = ai_avg
    offset = 0
    not_found = arr[i] != 'a'
    while not_found or i-offset >= 0 or i+offset <= n-1: 
        if arr[i-offset] == 'a':
            not_found = False
            i = i-offset
            break
        elif i+offset <= n-1 and arr[i+offset] == 'a':
            not_found = False
            i = i+offset
            break
        offset += 1
    
    



if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = input()
        solve(a, n)
