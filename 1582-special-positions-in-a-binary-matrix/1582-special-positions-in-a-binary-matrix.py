class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        ans = 0
        col_cnt, row_cnt = [0] * m, [0] * n
        for i in range(n):
            for j in range(m):
                col_cnt[j] += mat[i][j]
                row_cnt[i] += mat[i][j]
        
        for i in range(n):
            for j in range(m):
                if (row_cnt[i] + col_cnt[j] == 2 and mat[i][j]):
                    ans += 1
        return ans