class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        n = len(colors)
        dp = [[-1] * 27 for _ in range(n + 1)]
        def solve(i, prev):
            if i >= n:
                return 0
            if dp[i][ord(prev) - ord('a')] != -1:
                return dp[i][ord(prev) - ord('a')]
            ans = 0
            
            if(colors[i] == prev):
                ans = solve(i + 1, prev) + neededTime[i]
            else: 
                ans = min(solve(i + 1, colors[i]), solve(i + 1, prev) + neededTime[i])
            dp[i][ord(prev) - ord('a')] = ans
            return ans
            
        return solve(0, '{')