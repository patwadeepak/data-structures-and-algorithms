# B. Villagers

def solve(a, n):
    a.sort(reverse=True)
    e = 0
    i = -1
    while i + 1 < len(a) - 1:
        i += 1
        e += a[i]
        a[i] -= a[i+1]
        a[i+1] = 0
        i += 1

    if len(a)%2 != 0:
        e += a[-1]
    
    print(e)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        solve(a, n)
