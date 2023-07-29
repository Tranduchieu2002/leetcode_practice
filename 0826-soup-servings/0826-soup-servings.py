class Solution:
    def __init__(self):
        self.serve = [[100, 0], [75, 25], [50,50],[25, 75]]
    def solve(self, A, B, dp):
        if(A <= 0 and B <= 0): return 0.5
        if(A <= 0): return 1.0
        if(B <= 0): return 0.0

        if(dp[A][B] != -1.0): return dp[A][B] 
        ans = 0.0
        for val in (self.serve):
            ans += self.solve(A - val[0], B - val[1], dp)
        dp[A][B] = ans / 4
        return dp[A][B]
    def soupServings(self, n: int) -> float:
        if(n > 4801): return 1.0
        dp = [[ -1.0 for _ in range(n + 1)] for _ in range(n + 1)]
        a = (n + 24) // 25
        ans = self.solve(n,n, dp)
        
        return ans
        