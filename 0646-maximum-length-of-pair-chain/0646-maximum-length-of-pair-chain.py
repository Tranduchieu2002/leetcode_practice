class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort()
        dp = [0] * (n)
        for i in range(n):
            (l, r) = pairs[i]
            dp[i] = 1
            for j in range(i):
                if l > pairs[j][1]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return dp[n - 1]