class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans = 0
        n =len(nums)
        for i in range(0, n // 2):
            ans = max(ans, nums[i] + nums[n - i- 1])
        return ans