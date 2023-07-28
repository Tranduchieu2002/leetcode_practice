class Solution:
    def __init__(self):
        self.dp = [[-1] * 23 for _ in range(23)]
    
    def solve(self,i: int, j: int, nums: List[int]) -> int:
        if(i > j):
            return 0
        if(i == j):
            return nums[i]
        if(self.dp[i][j] != -1): return self.dp[i][j]
        takeHead = nums[i] - self.solve(i + 1, j, nums)
        takeTail = nums[j] - self.solve(i, j - 1, nums)
        self.dp[i][j] = max(takeHead, takeTail)        
        return self.dp[i][j]
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        
        return self.solve(0, n - 1, nums) >= 0
        