class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n, m = len(word1), len(word2)
        @cache
        def solve(i, j):
            # if i >= n or j >= n:
            #     return 0
            if i == 0:
                return j
            if j == 0:
                return i
            if word1[i - 1] == word2[j - 1]:
                return solve(i - 1, j - 1)
            ans = 502
            insert = solve(i, j - 1)
            delete = solve(i - 1, j)
            replace = solve(i - 1, j - 1)
            ans = min(ans,insert, delete, replace) + 1
            return ans
            
        return solve(n, m)