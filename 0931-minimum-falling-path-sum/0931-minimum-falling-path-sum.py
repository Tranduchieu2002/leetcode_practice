class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * (m) for _ in range(n)]
        
        dp[0] = matrix[0]
        for i in range(1, n):
            
            for j in range(m):
                temp = float('inf')
                for (x, y) in ([(-1, -1), (-1, 0), (-1,1)]):
                    dx, dy = i + x, j + y
                    if dx < 0 or dx >= n or dy < 0 or dy >= m:
                        continue
                    temp = min(temp, dp[dx][dy] + matrix[i][j])
                
                dp[i][j] = temp
        
        return min(dp[n - 1])
