class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[1] * (n + 1) for _ in range(m + 1)]
        
        d = [[0, 1], [1,0]]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m-1][n-1]