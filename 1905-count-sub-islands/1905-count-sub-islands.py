class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n, m = len(grid1), len(grid2[0])
        ans = 0

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid2[i][j] == 0:
                return True

            grid2[i][j] = 0  # Mark this cell as visited

            is_sub_island = True
            if grid1[i][j] == 0:
                is_sub_island = False

            for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if not dfs(i + x, j + y):
                    is_sub_island = False

            return is_sub_island

        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1:
                    ans += dfs(i, j)

        return ans
