class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        ans = 0
        n =  len(nums)
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        
        while(left < right):
            
            mid =  (right - left) // 2 + left
            count , i = 0, 1

            while i < n:
                if nums[i] - nums[i - 1] <= mid:
                    count += 1
                    i += 1
                i += 1
            if count < p:
                left  = mid + 1
            else:
                right = mid
        
        return left
            