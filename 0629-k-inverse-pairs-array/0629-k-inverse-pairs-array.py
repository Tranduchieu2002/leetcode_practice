class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        
        dp = [[0] * 1001 for _ in range(2)]
        dp[0][0] = 1
        
        mod = (10 ** 9) + 7
        
        for N in range(1, n + 1):
            for K in range(k + 1):
                if K > 0:
                    dp[N % 2][K] = (dp[(N - 1) % 2][K] + dp[N % 2][K - 1]) % mod
                else:
                    dp[N % 2][K] = (dp[(N - 1) % 2][K]) % mod

                if K >= N:
                    dp[N % 2][K] = (mod + dp[N % 2][K] - dp[(N - 1) % 2][K - N]) % mod
            

        return dp[n % 2][k]