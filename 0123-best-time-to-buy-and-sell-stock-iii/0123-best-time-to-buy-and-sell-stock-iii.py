class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]
        def solve(i, isBuy, timeTransactions = 2):
            
            if i >= n:
                return 0 
            if timeTransactions == 0:
                return 0
            if dp[i][isBuy][timeTransactions] != - 1:
                return dp[i][isBuy][timeTransactions]
            ans = 0
            if isBuy:
                ans = max(ans, 
                          solve(i + 1, False, timeTransactions) - prices[i], # buy
                          solve(i + 1,True, timeTransactions)) # dont buy
            else:
                ans = max(ans, 
                          solve(i + 1, True, timeTransactions - 1) + prices[i], # sell
                          solve(i + 1, False, timeTransactions)) # dont sell
            dp[i][isBuy][timeTransactions] = ans
            return ans
        
        return solve(0, True)