class Solution:
    def findPaths(self, n: int, m: int, maxMove: int, startRow: int, startColumn: int) -> int:
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        cnt = 0
        mod = 10 ** 9 + 7
        dp = [[0] * m for _ in range(n)]
        dp[startRow][startColumn] = 1

        for _ in range(maxMove):
            new_dp = [[0] * m for _ in range(n)]

            for i in range(n):
                for j in range(m):
                    for dx, dy in d:
                        ni, nj = i + dx, j + dy

                        if 0 <= ni < n and 0 <= nj < m:
                            new_dp[i][j] = (new_dp[i][j] + dp[ni][nj]) % mod
                        else:
                            # reach to limit
                            cnt = (cnt + dp[i][j]) % mod
            # print(new_dp)
            dp = new_dp

        return cnt

