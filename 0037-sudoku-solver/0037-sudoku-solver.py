class Solution:
    def check(self, row, col, k, board):
        for i in range(9):
            
            if board[row][i] == k: 
                return False
            if board[i][col] == k:
                return False
        start_row = row - (row % 3)
        start_col = col - (col % 3)
        
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):    
                if board[i][j] == k:
                    return False
        return True
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    continue
                for k in range(1, 10):
                    k = str(k)
                    isValidK = self.check(i, j, k, board)
                    if(isValidK):
                        board[i][j] = k
                        if self.solveSudoku(board):
                            return True
                        else:
                            board[i][j] = '.'
                return False
        return True