def solve(n, s):
    a = 0
    b = 0

    prefix_a = [0]*n
    prefix_b = [0]*n

    for i, ch in enumerate(s):
        if ch == 'a':
            a += 1
            prefix_a[i] = a
        else:
            prefix_a[i] = prefix_a[i-1] if i-1>=0 else 0

        if ch == 'b':
            b += 1
            prefix_b[i] = b
        else:
            prefix_b[i] = prefix_b[i-1] if i-1>=0 else 0
    
    w = abs(a - b)
    if w == 0:
        return 0
    
    for ws in range(w, n+1):
        for l in range(0, n-ws+1):
            r = l + ws - 1
            if l-1 >= 0:
                num_a = prefix_a[r] - prefix_a[l-1]
            else:
                num_a = prefix_a[r]

            if l-1 >= 0:
                num_b = prefix_b[r] - prefix_b[l-1]
            else:
                num_b = prefix_b[r]
            
            if (a - num_a) == (b - num_b):
                return num_a + num_b


if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        s = input()
        output = solve(n, s)
        print(-1 if n == output else output)
        t -= 1
    
"""
Using a prefix array is fast enougha and this is giving TLE.
Results are correct by this code. But I knew this would require
a solution with single loop.
"""