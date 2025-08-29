# B. Like the Bitset

def solve(n, k, s):
    maxx = -1
    max_1s = 0
    all_zero = True
    for ch in s:
        if ch == '1':
            all_zero = False
            max_1s += 1
            maxx = max(max_1s, maxx)
        else:
            max_1s = 0
 
    if all_zero:
        print('YES')
        print(*list(range(1, n+1)))
        return

    if not (maxx < k):
        print('NO')
    else:
        s = list(s)
        i = 0
        p = list(range(1, n+1))

        while i < len(s):
            if s[i] == '0':
                s[i] = p.pop()
            i += 1

        i = 0
        p = p[::-1]
        while i < len(s):
            if s[i] == '1':
                s[i] = p.pop()
            i += 1

        print('YES')
        print(*s)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, k = list(map(int, input().split(' ')))
        s = input()
        solve(n, k, s)
