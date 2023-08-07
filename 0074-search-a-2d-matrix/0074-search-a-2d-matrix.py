class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        
        if(n == 1):
            for colVal in matrix[0]:
                if(colVal == target): return True
            return False
        
        left , right = 0, n - 1
        
        inRow: int = -1
        
        while(left <= right):
            mid = (right - left) // 2 + left
            print(mid)
            if matrix[mid][0] == target:
                return True
            
            if matrix[mid][-1] == target:
                return True
            
            if matrix[mid][0] < target and matrix[mid][-1] > target:
                inRow = mid
                
            if matrix[mid][0] > target:
                right = mid - 1  
            else:
                left = mid + 1
            
        
        if(inRow == -1): return False
        
        for colVal in matrix[inRow]:
            
            if(colVal == target): return True
        
        return False
            
            
        