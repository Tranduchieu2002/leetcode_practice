class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        
        if n == 1:
            return target in matrix[0]
        
        left, right = 0, n - 1
        inRow = -1
        
        while left <= right:
            mid = (right - left) // 2 + left
            
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                inRow = mid
                break
            
            if matrix[mid][0] > target:
                right = mid - 1  
            else:
                left = mid + 1
        
        if inRow == -1:
            return False
        
        return target in matrix[inRow]
