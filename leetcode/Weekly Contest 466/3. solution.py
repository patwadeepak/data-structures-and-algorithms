from typing import List

def bowlSubarrays(A: List[int]) -> int:
    res = 0
    s = []
    for r, a in enumerate(A):
        while s and A[s[-1]] <= a:
            l = s.pop()
            if r - l + 1 >= 3:
                res += 1
        if s and r - s[-1] + 1 >= 3:
            res += 1
        s.append(r)
    return res

if __name__ == '__main__':
    A = [2,5,3,1,4]
    print(bowlSubarrays(A))
