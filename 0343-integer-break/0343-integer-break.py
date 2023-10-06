class Solution:
    def integerBreak(self, n: int) -> int:
        
        ans = 0
        dp = [[-1] * (n + 1) for _ in range(n + 1)]
        
        def solve(i, target):

            if i > target:
                return 1
            if target == 0: 
                return 1
            if i >= n: 
                return 0
            if dp[i][target] != -1:
                return dp[i][target] 
            ans = 0
            
            ans = max(ans, i * solve(i, target - i), solve(i + 1, target) )
            dp[i][target] = ans
            return ans
        
        return solve(1, n)
            