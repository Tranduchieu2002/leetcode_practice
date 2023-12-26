mod = 10 ** 9 + 7
print(mod)
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        dp = [[-1] * (target + 1) for _ in range(n + 1)]
        if n * k < target:
            return 0
        def solve(i, res):
            if res == 0 and i == 0:
                return 1
            if i <= 0:
                return 0
            if res < 0:
                return 0
            if dp[i][res] != -1:
                return dp[i][res]
            ans = 0
            for j in range(1, k + 1):
                if res < j:
                    break
                ans = (ans + (solve(i - 1, res - j) % mod)) % mod
            dp[i][res]  = ans
            return ans
        return solve(n, target)