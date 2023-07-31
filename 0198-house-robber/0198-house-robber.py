class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(n == 1): return nums[0]
        dp = [0, 0]
        for i in nums:
            dp.append(max(i + dp[-2], dp[-1]))
        return dp[-1]