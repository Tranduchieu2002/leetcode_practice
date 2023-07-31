class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        if (n == 0):
            return 0;
        
        if (n == 1):
            return nums[0];
        
        buckets = [0] * 100001
        dp = [0] * 10001
        for val in nums:
            buckets[val] += val
        # if nums is [2, 2, 3, 3, 3, 4] then buckets would be [0, 0, 4, 9, 4]
        # dp[2] => { 0;1 } = {4, 0}
        # dp[3] => { 1;2 } = {0, 9}
        # dp[4] => { 2;3 } = {4 + 4, 9} => ans = 9
    
        dp[0] = buckets[0]
        dp[1] = max(buckets[0], buckets[1]);
        for i in range(2,10001):
            dp[i] = max(dp[i - 1], dp[i - 2] + buckets[i])
        print(set(buckets))
        return dp[10000]
        