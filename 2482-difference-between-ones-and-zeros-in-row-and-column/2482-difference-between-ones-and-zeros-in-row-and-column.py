class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        ans = []
        
        def sumalize(nums):
            val = sum(nums)
            return val - (len(nums) - val)
        # cols = list(map(summation, zip(*grid)))
        col_sum = (list(map(sumalize,zip(*grid))))
        row_sum = (list(map(sumalize, grid)))
        
        for row in range(len(grid)):
            temp = []
            for col in range(len(grid[0])):
                temp.append(col_sum[col] + row_sum[row])
            ans.append(temp)
        return ans