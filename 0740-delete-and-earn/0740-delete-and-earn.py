class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        maxEle = max(nums)
        if (n == 0):
            return 0;
        
        if (n == 1):
            return nums[0];
        
        buckets = [0] * (maxEle + 1)
        # dp = [0] * 10001
        for val in nums:
            buckets[val] += val
        # if nums is [2, 2, 3, 3, 3, 4] then buckets would be [0, 0, 4, 9, 4]
        # dp[2] => { 0;1 } = {4, 0}
        # dp[3] => { 1;2 } = {0, 9}
        # dp[4] => { 2;3 } = {4 + 4, 9} => ans = 9
    
        # prev code
        # dp[0] = buckets[0]
        # dp[1] = max(buckets[0], buckets[1]);
        
        # another way using two vars to save first element dp, and second dp and then compare it
        #   [0, 0, 4, 9, 4]
        #   prev = curr = 0
        #   temp = 4 prev = 0, curr = 4
        #   temp = max(9,4) = 9, prev = 4, curr = 9
        #   temp = max(4 + 4, 9) = 9, prev = 9, curr = 9
        prev = curr = 0
        for i in range(maxEle + 1):
            # dp[i] = max(dp[i - 1], dp[i - 2] + buckets[i])            
            # way 2
            temp =  max(prev + buckets[i], curr)
            prev = curr
            curr = temp
        return curr
        