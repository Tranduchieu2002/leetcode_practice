class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n =  len(nums)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n):
            partition_idx = i + 1
            if nums[i] == nums[i - 1]:
               dp[partition_idx] |= dp[i - 1]
            
            if i > 1 and nums[i - 1] == nums[i] == nums[i - 2]:
                dp[partition_idx] |= dp[i - 2]
            
            if i > 1 and nums[i - 1] + 1 == nums[i] == nums[i - 2] + 2:
                dp[partition_idx] |= dp[i - 2]
        return dp[n]