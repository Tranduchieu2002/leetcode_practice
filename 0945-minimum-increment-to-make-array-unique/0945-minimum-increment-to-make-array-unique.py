class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        nxt = nums[0] + 1
        for i in range(1, len(nums)):
            if nxt >= nums[i]:
                ans += (nxt - nums[i])
                nxt += 1
            else:
                nxt = nums[i] + 1
        return ans