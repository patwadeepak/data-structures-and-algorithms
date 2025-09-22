from collections import defaultdict

def solve(n, m, sets):
    s = tuple(range(1, m+1))

    if n == 2:
        return 'Yes' if sets[0] == s and sets[1] == s else 'No'

    d = defaultdict(list)
    for i, a in enumerate(sets):
        for item in a:
            d[item].append(i)

    all_union = list(d.keys())
    all_union.sort()
    all_union = tuple(all_union)
    if all_union != s:
        return 'No'
    
    look = set(s)

    keys = list(d.keys())
    keys.sort(key=lambda x: len(d[x]))

    if len(d[keys[0]]) >= 2:
        return 'Yes'
    else:
        for key in keys:
            if len(d[key]) == 1:
                look = look - set(sets[d[key][0]])
        
        if len(look) == 0:
            return 'No'
        else:
            return 'Yes'

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, m = list(map(int, input().split(' ')))
        sets = []
        for _ in range(n):
            _, *s = map(int, input().split())
            sets.append(tuple(s))
        print(solve(n, m, sets))

"""
I have not looked at the solution or editorial yet.
But it feels like this is correct solution
with some edge cases misssing that is giving WA.
"""