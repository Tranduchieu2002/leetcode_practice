MOD = 1e9 + 7
class Solution:
    def countOrders(self, n: int) -> int:
        dp = 1
        for i in range(2, n + 1):
            dp = (dp * (2 * i - 1) * i) % MOD
        return int(dp)