class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left = - (10 ** 4 + 1)
        right = 10 ** 4 + 1
        
        while(left < right):
            mid = (right - left) // 2 + left
            
            count = 0
            for val in nums: 
                if(val > mid): 
                    count += 1
                
            if(count < k):
                right = mid
            else:
                left = mid + 1
        return left