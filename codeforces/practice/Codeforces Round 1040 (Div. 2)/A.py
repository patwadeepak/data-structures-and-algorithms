# A. Submission is All You Need

from typing import List
from collections import Counter


def get_freq_map(arr):
    return Counter(arr)


def get_missing_num(counter):
    missing_num = None
    for num in range(51):
        if counter[num] == 0:
            missing_num = num
            break
    return missing_num

def get_sum(counter, missing_num):
    score = 0
    counterKeys = list(counter.keys())
    mex_added = False
    for key in counterKeys:
        if key > missing_num:
            count = counter.pop(key)
            score += count*key
        elif counter[key] > 0:
            counter[key] -= 1
            if not mex_added:
                score += missing_num
                mex_added = True
    return score, counter


def calculate_score(freq_map):
    # base case, if all values in freq_map are zero then return 0 score.
    non_zero_found = False
    for key in freq_map.keys():
        if freq_map[key] > 0:
            non_zero_found = True
            break
 
    if not non_zero_found:
        return 0

    missing_num = get_missing_num(freq_map)

    score, freq_map = get_sum(freq_map, missing_num)

    return score + calculate_score(freq_map)


def solve(arr: List[int], n: int) -> None:
    freq_map = get_freq_map(arr)
    
    score = calculate_score(freq_map)

    print(score)


if __name__ == '__main__':
    """
    This is incorrect for few cases.
    The solution is almost there. But I am damn sure that there is a much much simpler
    solution out there. Which will definitely open my understanding to better solutions.
    """
    t = int(input())

    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split(' ')))
        solve(arr, n)

