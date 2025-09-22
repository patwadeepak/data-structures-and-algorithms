from collections import Counter

def solve(a, n):
    c = Counter(a)    

    maxx = float('-inf')
    for key in c.keys():
        maxx = max(maxx, c[key])

    min_removal = float('inf')
    for m in range(maxx, 0, -1):
        removal = 0
        for key in c.keys():
            if m > c[key]:
                removal += c[key]
            elif m < c[key]:
                removal += c[key] - m
        min_removal = min(min_removal, removal)
    
    return n-min_removal

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        print(solve(a, n))
