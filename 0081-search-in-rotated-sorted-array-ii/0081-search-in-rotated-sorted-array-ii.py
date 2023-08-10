class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums = list(set(nums))
        n = len(nums)
        left, right = 0 , n - 1
        while(left <= right):
            mid = (right + left) // 2
            if(nums[mid] == target): return True;  
            if(nums[mid] >= nums[left]):
                if(target <= nums[mid] and target >= nums[left]):
                    right = mid - 1
                else:   
                    left = mid + 1
            else:
                if(target >= nums[mid] and target <= nums[right]):
                    left = mid + 1
                else:
                    right = mid - 1
        return False