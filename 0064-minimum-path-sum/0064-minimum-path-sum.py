inf = float('inf')
ninf = 0 - float('inf')

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        d = [(1, 0), (0, 1)]
        dp = [[-1] * 201 for _ in range(201)] 
        def solve(i, j):
            if i >= n or j >= m:
                return inf
            if i >= n - 1 and j >= m - 1:
                return grid[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            ans = inf
            for (x, y) in d:
                dx = i + x
                dy = j + y
                
                ans = min(solve(dx, dy) + grid[i][j], ans)
            dp[i][j] = ans
            return ans
        res = solve(0,0)
        return -1 if res  == inf  else res