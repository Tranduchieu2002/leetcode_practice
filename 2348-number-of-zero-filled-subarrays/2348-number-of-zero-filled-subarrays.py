class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        cnt = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                cnt += 1
                ans += cnt
            else:
                cnt = 0
        return ans
        