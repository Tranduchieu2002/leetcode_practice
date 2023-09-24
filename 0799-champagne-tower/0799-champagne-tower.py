class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [0] * (query_row + 1)
        dp[0] = poured
        for i in range(1, query_row + 1):
            for j in range(query_row, -1, -1):
                # dp[j] = max(0.0, (dp[j + 1] - 1) / 2)
                dp[j] = max(0.0, (dp[j - 1] - 1) / 2) + max(0.0, (dp[j] - 1) / 2)
            # print(dp)
        
        return min(dp[query_glass], 1.0)
            
            