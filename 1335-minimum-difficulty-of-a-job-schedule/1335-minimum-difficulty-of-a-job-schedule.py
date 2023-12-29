INF = float('inf')
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        @cache
        def solve(i, k):
            if k < 0:
                return INF
            if k == 0 or i == n:
                if i == n and k == 0:
                    return 0
                return INF
            maxDiffJobInOneDay = 0
            res = INF
            for j in range(i, n - k + 1):  # Fix loop range
                maxDiffJobInOneDay = max(maxDiffJobInOneDay, jobDifficulty[j])
                res = min(res, maxDiffJobInOneDay + solve(j + 1, k - 1))
            return res
        ans = solve(0, d)
        if ans == INF:
            return -1
        return ans
