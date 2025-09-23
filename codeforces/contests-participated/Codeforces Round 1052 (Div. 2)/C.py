def solve(s, n):
    arr = []
    ones = 0
    for i, si in enumerate(s, start=1):
        if si == '1':
            ones += 1
            if i-2 >= 0 and s[i-2] == '0':
                arr.extend(list(range(i-1, len(arr), -1)))
            arr.append(i)
        else:
            if (i-2 >= 0 and s[i-2] == '0') or (i < n and s[i] == '0'):
                pass
            else:
                print('NO')
                return

    print('YES')
    if ones == 0:
        print(*list(range(n, 0, -1)))
    else:
        if len(arr) < n and s[n-1] == '0':
            arr.extend(list(range(n, len(arr), -1)))
        print(*arr)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        s = input()
        solve(s, n)

"""
Solved After Contest.
my very own solution.
Looking at editorial's solution this looks better.
But it seems that both have same complexity of O(n)
"""