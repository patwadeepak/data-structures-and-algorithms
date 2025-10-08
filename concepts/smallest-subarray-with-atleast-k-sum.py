# https://www.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1

class Solution:
    def smallestSubWithSum(self, x, arr):
        n = len(arr)
        s = arr[0]
        ans = float('inf')
        l = 0
        r = 0
        while l<=r and r<n:
            if s > x:
                ans = min(r-l+1, ans)
                if r == l:
                    # earlier I was increasing r and l both by one for this case
                    # it turns out 1 is minimum possible answer. so we can just return
                    return 1
                else:
                    s -= arr[l]
                    l += 1
            else:
                r += 1
                if r<n:
                    s += arr[r]
        
        return 0 if ans == float('inf') else ans

if __name__=="__main__":
    s = Solution()
    result = s.smallestSubWithSum(51, [1,4,45,6,0,19])
    print(result)
