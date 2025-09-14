import math

def solve(a, n):
    is_any_odd = any([x%2 == 1 for x in a])
    if not is_any_odd:
        return 0
    
    odds = []
    score = 0
    for num in a:
        if num % 2 == 0:
            score += num
        else:
            odds.append(num)
    
    odds.sort()

    largest_odd = odds.pop()
    score += largest_odd

    if len(odds)%2 == 0:
        score += sum(odds[len(odds)//2:])
    else:
        start = int(math.ceil(len(odds)/2))
        score += sum(odds[start:])
    return score

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        a = list(map(int, input().split(' ')))
        print(solve(a, n))
