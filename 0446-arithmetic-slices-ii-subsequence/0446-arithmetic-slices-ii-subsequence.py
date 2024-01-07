class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        n = len(nums)
        ans = 0
        dp = [{} for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                # print(f"CanGetPrev: i = {nums[i]}, j = {nums[j]}, diff = {diff}", dp[j].get(diff, 0))
                dp[i][diff] = dp[i].get(diff, 0) + dp[j].get(diff, 0) + 1
                ans += dp[j].get(diff, 0)
            # print(dp)
        return ans