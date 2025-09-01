# https://www.geeksforgeeks.org/problems/subset-sum-problem2014/1

class Solution:
    def equalPartition(self, arr):
        self.memo = {}
        self.arr = arr
        s = sum(arr)
        if s%2 != 0:
            return False
        return self.equalPartitionRec(len(arr), s//2)

    def equalPartitionRec(self, n, s):
        if s == 0:
            return True
        if n == 0:
            return False

        m = self.memo.get((n, s))
        if m is not None:
            return m

        if s - self.arr[n-1] >= 0:
            pick = self.equalPartitionRec(n-1, s-self.arr[n-1])
            not_pick = self.equalPartitionRec(n-1, s)
            res = pick or not_pick
        else:
            res = self.equalPartitionRec(n-1, s)
        
        self.memo[(n,s)] = res

        return res


if __name__=='__main__':
    s = Solution()

    arr = [1, 6, 12, 5]
    print(s.equalPartition(arr))

"""
Great progress for me. Provided this was essentially subset sum problem only :)
But happy that I could solve this easily now without checking any solutions
or editorial or looking at any code. 
"""
