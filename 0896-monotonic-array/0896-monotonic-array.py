class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isDecrease, isIncrease = False, False
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                isIncrease = True
            if  nums[i - 1] > nums[i]:
                isDecrease = True
            if isIncrease and isDecrease:
                return False
        
        return True