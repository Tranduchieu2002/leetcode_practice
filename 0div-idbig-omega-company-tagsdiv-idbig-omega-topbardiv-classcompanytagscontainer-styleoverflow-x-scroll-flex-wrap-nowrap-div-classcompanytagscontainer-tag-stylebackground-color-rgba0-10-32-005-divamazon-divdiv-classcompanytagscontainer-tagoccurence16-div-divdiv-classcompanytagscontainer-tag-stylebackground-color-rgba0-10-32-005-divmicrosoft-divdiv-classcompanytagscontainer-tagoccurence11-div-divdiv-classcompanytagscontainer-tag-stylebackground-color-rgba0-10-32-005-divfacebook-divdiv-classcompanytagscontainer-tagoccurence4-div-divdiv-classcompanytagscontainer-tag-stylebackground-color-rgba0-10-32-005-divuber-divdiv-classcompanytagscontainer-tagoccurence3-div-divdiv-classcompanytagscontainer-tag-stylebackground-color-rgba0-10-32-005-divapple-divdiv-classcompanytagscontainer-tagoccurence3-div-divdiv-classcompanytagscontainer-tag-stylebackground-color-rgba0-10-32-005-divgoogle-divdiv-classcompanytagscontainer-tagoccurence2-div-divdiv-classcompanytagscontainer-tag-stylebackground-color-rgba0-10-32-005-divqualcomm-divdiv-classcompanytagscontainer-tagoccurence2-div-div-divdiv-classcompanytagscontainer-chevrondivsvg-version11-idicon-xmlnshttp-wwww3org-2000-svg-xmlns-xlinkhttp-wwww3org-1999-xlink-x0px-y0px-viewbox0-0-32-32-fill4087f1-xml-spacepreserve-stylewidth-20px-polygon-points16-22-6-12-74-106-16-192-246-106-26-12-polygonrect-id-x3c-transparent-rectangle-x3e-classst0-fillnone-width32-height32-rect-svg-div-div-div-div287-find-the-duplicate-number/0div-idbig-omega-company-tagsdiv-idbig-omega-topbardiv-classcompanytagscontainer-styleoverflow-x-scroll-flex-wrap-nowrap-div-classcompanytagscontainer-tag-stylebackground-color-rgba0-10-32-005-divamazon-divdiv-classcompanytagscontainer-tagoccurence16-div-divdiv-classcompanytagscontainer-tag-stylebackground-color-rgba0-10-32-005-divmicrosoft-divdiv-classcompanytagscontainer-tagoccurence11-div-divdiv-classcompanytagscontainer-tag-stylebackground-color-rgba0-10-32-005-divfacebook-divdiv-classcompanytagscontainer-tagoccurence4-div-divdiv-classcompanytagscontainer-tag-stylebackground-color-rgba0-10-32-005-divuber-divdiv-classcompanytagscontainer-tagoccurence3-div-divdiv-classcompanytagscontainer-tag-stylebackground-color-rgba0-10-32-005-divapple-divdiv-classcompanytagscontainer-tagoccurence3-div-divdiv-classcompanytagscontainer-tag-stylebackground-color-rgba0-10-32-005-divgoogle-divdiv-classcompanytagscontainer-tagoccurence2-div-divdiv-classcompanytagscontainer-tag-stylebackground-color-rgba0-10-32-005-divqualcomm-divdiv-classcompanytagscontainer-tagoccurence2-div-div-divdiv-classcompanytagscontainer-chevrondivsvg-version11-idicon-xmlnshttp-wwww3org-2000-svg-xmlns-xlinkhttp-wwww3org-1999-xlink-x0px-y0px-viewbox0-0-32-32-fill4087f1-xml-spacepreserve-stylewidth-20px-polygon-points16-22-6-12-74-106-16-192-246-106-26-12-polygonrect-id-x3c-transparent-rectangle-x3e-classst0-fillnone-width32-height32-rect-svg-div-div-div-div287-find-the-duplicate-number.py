class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        prev_num = -1
        for num in nums:
            if prev_num == num:
                return num
            prev_num = num
        return -1