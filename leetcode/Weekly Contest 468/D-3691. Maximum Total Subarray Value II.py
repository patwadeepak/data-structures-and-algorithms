class Solution:
    def maxTotalValue(self, nums, k: int) -> int:
        maxx = float('-inf')
        minn = float('inf')

        for i, num in enumerate(nums):
            if maxx <= num:
                maxx = max(maxx, num)
                mxi = i
            if minn > num:
                minn = min(minn, num)
                mni = i

        n = len(nums)
        l = 0
        r = n-1
        i = 0
        value = 0

        while i < k and l < r:
            value += maxx - minn

            if mni < mxi:
                if mni - l == 0 and r - mxi == 0:
                    maxx_new = float('-inf')
                    minn_new = float('inf')
                    mxi_new = None
                    mni_new = None
                    if r - l - 1 > 0:
                        for x, num in enumerate(nums[l+1:r], start=l+1):
                            if maxx_new <= num:
                                maxx_new = max(maxx_new, num)
                                mxi_new = x
                            if minn_new > num:
                                minn_new = min(minn_new, num)
                                mni_new = x
                        if maxx - maxx_new > minn_new - minn:
                            minn = minn_new
                            mni = mni_new
                            l += 1
                        else:
                            maxx = maxx_new
                            mxi = mxi_new
                            r -= 1
                    else:
                        break
                else:
                    if mni - l > r - mxi:
                        l += 1
                    else:
                        r -= 1
            else:
                if mxi - l != 0 and r - mni != 0:
                    maxx = float('-inf')
                    minn = float('inf')
                    mxi_new = None
                    mni_new = None
                    if r - l - 1 > 0:
                        for x, num in enumerate(nums[l+1:r], start=l+1):
                            if maxx <= num:
                                maxx = max(maxx, num)
                                mxi = x
                            if minn > num:
                                minn = min(minn, num)
                                mni = x
                        if maxx - maxx_new > minn_new - minn:
                            minn = minn_new
                            mni = mni_new
                            r -= 1
                        else:
                            maxx = maxx_new
                            mxi = mxi_new
                            l += 1
                    else:
                        break
                else:
                    if mxi - l > r - mni:
                        l += 1
                    else:
                        r -= 1

            i += 1

        return value

if __name__ == '__main__':
    s = Solution()

    op = s.maxTotalValue([9,9,37], 3)
    print(op)

"""
Not a solution. Just an attempt.
"""