class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = sum(nums)
        prev = 0
        ans = []
        
        for i in range(n):
            sum_prev_i = (nums[i] * i) - prev
                
            sum_after_i = (total - prev - nums[i]) - (nums[i] * (n - i - 1)) 
            
            ans.append(sum_prev_i + sum_after_i)
            
            prev += nums[i]
        return ans