from collections import deque

def solve(n, m, s, a):
    new_black = deque()
    black = a[::-1]
    a = set(a)
    p = 1
    for si in s:
        if si == 'B':
            while black and black[-1] < p:
                black.pop()
            if black and new_black:
                if black[-1] < new_black[0]:
                    if p+1 == black[-1]:
                        p = black.pop() + 1
                    else:
                        p += 1
                else:
                    if p+1 == new_black[0]:
                        p = 1 + new_black.popleft()
                    else:
                        p += 1
            elif black:
                if p+1 == black[-1]:
                    p = black.pop() + 1
                else:
                    p += 1
            elif new_black:
                if p+1 == new_black[0]:
                    p = 1 + new_black.popleft()
                else:
                    p += 1
            else:
                p += 1
            new_black.append(p)
            a.add(p)
            while p in a:
                p += 1
        else:
            p += 1
            new_black.append(p)
            a.add(p)

    res = list(set(a))
    res.sort()
    print(len(res))
    print(*res)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, m  = list(map(int, input().split()))
        s = input()
        a  = list(map(int, input().split()))
        solve(n, m, s, a)
