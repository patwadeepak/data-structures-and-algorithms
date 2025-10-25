from typing import List

class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        n,m = len(mat),len(mat[0])
        
        if n > 35:
            return 0

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149]

        set_primes = set(primes)

        n * m
                        
        # how to solve this ??

# hopefully I will upsolve this one day on my own.
