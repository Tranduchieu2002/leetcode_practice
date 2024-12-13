class Solution:
    def findScore(self, nums: List[int]) -> int:
        N = 10 ** 6
        n = len(nums)
        
        # This is chosen as 20 because shifting nums[i] << 20 + i creates a unique encoding.
        BASE_MARK = 20
        nthI = [0] * n
        mark = [False] * n
        for i, val in enumerate(nums):
            nthI[i] = ((val << BASE_MARK) + i)
        nthI.sort()
        ans = 0
        for val in nthI:
            
            x = val >> BASE_MARK
            i = val & ((1 << BASE_MARK) - 1)
            if mark[i]:
                continue
            
            mark[i] =  True
            ans += x
            if i > 0:
                mark[i - 1] = True
            if i < n - 1:
                mark[i + 1] = True
        return ans