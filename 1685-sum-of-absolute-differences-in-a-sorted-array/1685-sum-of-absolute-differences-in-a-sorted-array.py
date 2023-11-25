class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [nums[0]]
        ans = []
        
        for i in range(1, len(nums)):
            pref.append(pref[i - 1] + nums[i])
        
        for i in range(n):
            sum_before_i = 0
            if i > 0:
                sum_before_i =(nums[i] * i) - pref[i -1] 
                
            sum_after_i = -(nums[i] * (n - i - 1))  + (pref[n - 1] - pref[i])
            
            ans.append(sum_before_i + sum_after_i)
        
        return ans