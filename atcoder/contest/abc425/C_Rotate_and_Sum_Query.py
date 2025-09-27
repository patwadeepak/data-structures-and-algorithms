s = None
off = 0
n = None

def solve():
    q, *v = list(map(int, input().split()))
    global off
    if q == 1:
        off += v[0]
    else:
        l, r = v
        N = r-l+1
        l = (l - 1 + off)%n
        r = (r - 1 + off)%n

        if r<l and l-1 >= 0:
            value = s[r] + s[l] - s[l-1]
        elif l-1 >= 0:
            value = s[r] - s[l-1]
        else:
            value = s[r]
        print(value)

if __name__ == '__main__':
    n, q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    s = [0]*n

    total = 0
    for i, ai in enumerate(a):
        total += ai
        s[i] = total
    
    for _ in range(q):
        solve()
"""
Passes only 8 test cases and fails the rest with WA
TIL somthing new. Rotating the array creates 
a possibility for ranges across the boundary of 1 & n

To overcome this naturally without much calculation.
We calculate the sum array on 1 2 3 4 1 2 3 4,
2 copies of array concatenated together.

Pretty slick technique imo.
"""
