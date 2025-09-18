import copy
from typing import List
from collections import Counter

def solve(n, k, a: List[int], b):
    a.sort(reverse=True)
    c = Counter(b)

    b_vals = sorted(list(c.keys()))

    cost = 0

    i = 0
    curr_b_value = copy.deepcopy(b_vals[i])
    original_b_value = copy.deepcopy(b_vals[i])
    for item in a:
        if curr_b_value == 0:
            c[original_b_value] -= 1
            if c[original_b_value] != 0:
                curr_b_value = copy.deepcopy(b_vals[i])
                original_b_value = copy.deepcopy(b_vals[i])
            else:
                i += 1
                if i >= len(b_vals):
                    curr_b_value = float('inf')
                else:
                    curr_b_value = copy.deepcopy(b_vals[i])
                    original_b_value = copy.deepcopy(b_vals[i])
        
        if curr_b_value > 1:
            cost += item
        
        curr_b_value -= 1
 
    return cost

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n, k = list(map(int, input().split(' ')))
        a = list(map(int, input().split(' ')))
        b = list(map(int, input().split(' ')))
        print(solve(n, k, a, b))
