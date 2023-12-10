class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * 101
        
        def solve(i, dp, isTakeLast = False):
            
            if isTakeLast and i == n - 1:
                return nums[n - 1]
            
            if i >= n:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            ans = 0
            
            take = solve(i + 2, dp, isTakeLast) + nums[i]
            dontTake = solve(i + 1, dp, isTakeLast)
            ans = max(take, dontTake)
            
            dp[i] = ans
            return ans
        notTakeFirst = solve(1, memo)
        memo = [-1] * 101
        memo[n - 1] = 0
        takeFirst = solve(0, memo)

        return max(takeFirst, notTakeFirst, nums[0])