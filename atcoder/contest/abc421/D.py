def solve(rt, ct, ra, ca, n, m, ll):
    t = [rt, ct]
    a = [ra, ca]

    moves_t = []
    for _ in range(m):
        sm, am = input().split(' ')
        am = int(am)
        moves_t.append([sm, am])

    moves_a = []
    for _ in range(ll):
        tl, bl = input().split(' ')
        bl = int(bl)
        moves_a.append([tl, bl])
    
    same_cell = 0
    
    ti = 0
    ai = 0
    sm, am = moves_t[ti]
    tl, bl = moves_a[ai]
    for _ in range(n):

        if sm == 'U':
            t[0] -= 1
        elif sm == 'D':
            t[0] += 1
        elif sm == 'R':
            t[1] += 1
        elif sm == 'L':
            t[1] -= 1

        if tl == 'U':
            a[0] -= 1
        elif tl == 'D':
            a[0] += 1
        elif tl == 'R':
            a[1] += 1
        elif tl == 'L':
            a[1] -= 1
        
        if t == a:
            same_cell += 1
        
        if _ == n-1:
            break

        am -= 1
        if am == 0:
            ti += 1
            sm, am = moves_t[ti]
        
        bl -= 1
        if bl == 0:
            ai += 1
            tl, bl = moves_a[ai]
    
    print(same_cell)
    
if __name__ == '__main__':
    rt, ct, ra, ca = map(int, input().split(' '))
    n, m, ll = map(int, input().split(' '))
    
    solve(rt, ct, ra, ca, n, m, ll)

"""
This is incorrect since this is the simulation of the
process mentioned in the problem. So, obviously it would TLE.
I will try to come up with a solution for this.
"""
