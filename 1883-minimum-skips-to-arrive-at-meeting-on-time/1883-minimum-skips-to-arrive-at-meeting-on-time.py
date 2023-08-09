class Solution:
    def __init__(self):
        self.speed = -1
    def my_ceil(self, d):
        return ceil(d / self.speed) * self.speed
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        self.speed = speed
        min_dist_target = speed * hoursBefore
        
        dp = [[-1] * n for _ in range(n)]
        
        dp[0][0] = dist[0]

        for i in range(1, n):
            dp[i][0] = self.my_ceil(dp[i - 1][0]) + dist[i]
            # none resting
            for j in range(1, i):
                dp[i][j] = min(self.my_ceil(dp[i - 1][j]) ,(dp[i - 1][j - 1])) + dist[i]
            dp[i][i] = (dp[i-1][i-1]) + dist[i]
        # print(dp) 
        for i in range(n):
            if(dp[-1][i]) <= min_dist_target:
                return i
        
        return -1
            