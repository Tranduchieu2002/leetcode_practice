class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        while left <= right and nums[left] <= nums[right]:
            pos = nums[left] * -1 if nums[left] < 0 else nums[left] 
            if nums[left] * -1 == nums[right]:
                return nums[right]
            if pos < nums[right]:
                right -= 1
            else:
                left += 1                
        return -1