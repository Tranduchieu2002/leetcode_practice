class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = defaultdict(int)
        ans = 0
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                hash_str = f"{j}-{diff}"
                ans += dp[hash_str]
                dp[f"{i}-{diff}"] += dp[hash_str] + 1
        # print(dp)
        return ans