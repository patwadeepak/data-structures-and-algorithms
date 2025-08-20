# A. Submission is All You Need

"""
S = {0, 1, 1, 3}

------ Strategy 1 -------------
S' = {3}

then -
score = 0
do -> score += sum(S')
score = 3
do -> S - S' = {0, 1, 1}

S' = {0, 1, 1}
mex(S') = 2

score += 2
score = 5

the end. Max Score 5 by this way


------ Strategy 2 -------------
S' = {3}

then -
score = 0
do -> score += sum(S')
score = 3
do -> S - S' = {0, 1, 1}

S' = {0, 1}
mex(S') = 2

score += 2
score = 5

S = {1}
S' = {1}
sum(S') = 1 
score += 1
score = 6

S = {}

the end. Max Score 6 by this way

"""

from typing import List
from collections import defaultdict

def solve(arr: List[int], n: int) -> None:
    num_set = set(arr)
    # find the missing non negative integer first
    missing_num = None
    for num in range(51):
        if num in num_set:
            continue
        else:
            missing_num = num
            break
    
    # now add all numbers bigger than that using sum operation in one go
    f = defaultdict(int)
    sum = 0
    for num in arr:
        if num > missing_num:
            sum += num
            num_set.discard(num)
        else:
            # calculate frequency of all the numbers less than the missing minimum number
            f[num] += 1

    # now lets add this sum to score
    score = sum

    # now we will try to get as many instances of mex as possible
    # to do this we need to have all the numbers till
    min_freq = min(*f.values())

    # (( m*(m+1)/2 ) + missing_num ) * min_freq

    m = missing_num - 1

    score_part_2 = ( (m * (m + 1)/2) + missing_num ) * min_freq

    if len(f.values()) == 0 or all(f.values()) == False:
        return score + score_part_2
    else:
        return score + score_part_2 + solve() # complete this later...


if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(arr, n)
