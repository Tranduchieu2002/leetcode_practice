class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        total_steps = 0
        start_point = (0, 0)
        d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        n, m = len(grid), len(grid[0])
        ans = 0
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    total_steps += 1
                if grid[i][j] == 1:
                    start_point = (i, j)
                if grid[i][j] == -1:
                    visited[i][j] = True


        def backtrack(i, j, counter):
            nonlocal ans  # Declare ans as a non-local variable
            if i < 0 or j < 0 or i >= n or j >= m or visited[i][j]:
                return
            if counter == total_steps + 1 and grid[i][j] == 2:
                ans += 1
                return

            visited[i][j] = True
            counter += 1
            for x, y in d:
                dx = x + i
                dy = y + j
                backtrack(dx, dy, counter)
            counter -= 1
            visited[i][j] = False


        backtrack(start_point[0], start_point[1], 0)
        return ans
