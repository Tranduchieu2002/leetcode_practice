class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = k, k
        min_val = nums[k]
        ans = nums[k]
        
        while left > 0 or right < (n - 1):
            
            if left == 0 or right < (n - 1) and nums[right + 1] > nums[left - 1]:
                right += 1
            else:
                left -= 1
                
            min_val = min(min_val, nums[right], nums[left])
            
            ans = max(ans, min_val * (right - left + 1))
        
        return ans
            
        
        