def find_max_index(p):
    maxx = float('-inf')
    max_index = None
    for i, num in enumerate(p):
        if maxx < num:
            maxx = num
            max_index = i
    return max_index

def solve(p, n):
    maxx_i = find_max_index(p)

    for i in range(n):
        if maxx_i == len(p)-1:
            pass
        elif p[maxx_i] == p[maxx_i+1] + 1:
            p.pop(maxx_i)
            continue
        
        if maxx_i == 0:
            pass
        elif p[maxx_i] == p[maxx_i-1] + 1:
            p.pop(maxx_i)
            maxx_i = maxx_i - 1
        
        if len(p) == 1 and p[0] == 1 and i == n-1:
            p = []

    return 'Yes' if len(p) == 0 else 'No'

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        p = list(map(int, input().split(' ')))
        print(solve(p, n))
