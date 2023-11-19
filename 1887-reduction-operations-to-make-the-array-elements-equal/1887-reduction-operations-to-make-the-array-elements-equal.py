class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        nums.sort(reverse= True)
        n = len(nums)
        cnt = 0
    
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                continue
            cnt += i
        return cnt