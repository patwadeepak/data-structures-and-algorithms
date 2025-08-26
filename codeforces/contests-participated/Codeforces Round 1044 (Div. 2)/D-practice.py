# D. Chicken Jockey

def get_damage(a, n, i):
    d = a[i]

    if i+1 < n:
        if a[i+1] <= i+1:
            d += a[i+1]
            if i+2 < n:
                d += get_damage(a[i+2:], len(a[i+2:]), 0)
        else:
            d += i+1
    return d


def solve(a, n):
    arrs = [a]
    a = 0
    i_arr = 0
    while arrs:
        arr = arrs[i_arr]
        i_max_d = -1
        max_d = float('-inf')
        for i in range(len(arr)):
            d = get_damage(arr, len(arr), i)
            if max_d < d:
                max_d = d
                i_max_d = i
        a += arr[i_max_d]

        part2 = None
        if i_max_d+1 < len(arr):
            arr[i_max_d+1] -= i_max_d+1
            if arr[i_max_d+1] > 0:
                part2 = arr[i_max_d+1:]
            elif i_max_d+2 < len(arr):
                part2 = arr[i_max_d+2:]

        arrs.pop(i_arr)
        part1 = arr[:i_max_d]
        if part1:
            arrs.append(part1)
        if part2:
            arrs.append(part2)

if __name__ == '__main__':
    "NOT A SOLUTION"
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        print(solve(a, n))
"""
This looks like a very very good problem to solve.
"""

"""
I realize, I need to polish my DP then attempt this again later.
"""