class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def isNotValid(i, j, v):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0 or v[i][j]:
                return True
            return False
        
        def dfs(g, v, i , j):
            if (isNotValid(i, j, v)):
                return 0
            ans = 0
            v[i][j] = True
            for x, y in d:
                dx, dy = i + x, j + y
                ans = max(ans, dfs(g, v, dx, dy) + g[i][j])
            v[i][j] = False
            return ans
        finalAns = 0
        v = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                finalAns = max(finalAns, dfs(grid, v, i, j))
        return finalAns