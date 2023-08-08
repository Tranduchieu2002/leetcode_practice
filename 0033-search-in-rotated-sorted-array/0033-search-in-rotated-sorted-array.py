class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        left, right = 0 , n - 1
        while(left <= right):
            mid = (right + left) // 2
            # print(left, mid, right)
            if(nums[mid] == target): return mid;  
            if(nums[mid] >= nums[left]):
                if(target <= nums[mid] and target >= nums[left]):
                    right = mid - 1
                else:   
                    left = mid + 1
            else:
                if(target <= nums[mid] or target >= nums[left]):
                    right = mid - 1
                else:
                    left = mid + 1
                    print('end')
        return -1
