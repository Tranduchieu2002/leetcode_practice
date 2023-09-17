class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        s = f = 0
        for i in range(n):
            s += nums[i]
            f += (nums[i] * i)
        ans = f
        for i in range(1, n):
            f = f - nums[(n - i)] * (n) + s
            ans = max(ans, f)
        return ans
            