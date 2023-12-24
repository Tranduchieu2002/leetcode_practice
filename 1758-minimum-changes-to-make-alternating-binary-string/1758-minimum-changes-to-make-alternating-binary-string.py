class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        dp = [[0,0] for _ in range(n)] # 0 is zores & 1 is ones
        
        # if(s[0] == '0'):
        #     dp[0][0], dp[0][1] = 1, 0
        # else:
        #     dp[0][0], dp[0][1] = 0, 1
        for i in range( n):
            if s[i] == '0':
                dp[i][1] = dp[i - 1][0]
                dp[i][0] = dp[i - 1][1] + 1
            else:
                dp[i][0] = dp[i - 1][1]
                dp[i][1] = dp[i - 1][0] + 1
        # print(dp)
        return min(dp[n - 1][0], dp[n - 1][1])