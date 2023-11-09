class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt, n = 0, len(nums)
        for i in range(0, n):
            if nums[i] != nums[cnt]:
                cnt += 1
                nums[cnt] = nums[i]
                print(cnt)
        return cnt  + 1
        