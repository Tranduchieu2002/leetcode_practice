class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n , m = len(matrix), len(matrix[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if i > 0 and matrix[i][j]:
                    matrix[i][j] += matrix[i - 1][j]
        for i in range(n):
            max_height_row = sorted(matrix[i], reverse=True)
            for j in range(m):
                ans = max(ans, max_height_row[j] * (j + 1))
            
        return ans