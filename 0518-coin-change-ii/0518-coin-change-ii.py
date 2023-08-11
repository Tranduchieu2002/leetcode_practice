class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for i in coins:
            
            if i > amount:
                continue
            for c in range(i, amount + 1):
                dp[c] += dp[c - i]
        print(dp)
        return dp[amount]