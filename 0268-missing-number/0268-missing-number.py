class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if nums[n - 1] == n - 1:
            return n
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] + 1 == mid:
                return mid
            
            if nums[mid] <= mid:
                left = mid + 1
            else:
                right = mid - 1
        return left
        