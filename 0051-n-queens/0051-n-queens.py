class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        matrix = [['.' for _ in range(n)] for _ in range(n)]
        ans = []
        def check(row, col):
            for i in range(n):
                if matrix[row][i] == 'Q':
                    return False
                if matrix[i][col] == 'Q':
                    return False
            
            for i in range(n):
                for j in range(n):
                    if abs(i - row) == abs(j - col) and matrix[i][j] == 'Q':
                        return False
            return True
                    
        
        def solve(i):
            print(i)
            if i == n:
                ans.append(["".join(row) for row in matrix])
                return
            for j in range(n):
                if(check(i, j)):
                    matrix[i][j] = 'Q'
                    solve(i + 1)
                    matrix[i][j] = '.'
        solve(0)
        return ans