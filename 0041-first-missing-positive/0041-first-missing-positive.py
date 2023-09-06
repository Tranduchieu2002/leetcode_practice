class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 or nums[i] > n:
                nums[i] = 0
        nums.sort()
        for i, val in enumerate(nums):
            nums[nums[i] % n] = -1
        for i in range(n):
            if nums[i] != -1:
                return i
        
        return n
        