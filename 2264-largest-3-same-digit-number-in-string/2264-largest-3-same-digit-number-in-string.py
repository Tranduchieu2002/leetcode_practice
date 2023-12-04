class Solution:
    def largestGoodInteger(self, nums: str) -> str:
        ans = None
        n = len(nums)
        count_so_far = 1
        for i in range(n - 1):
            if nums[i + 1] == nums[i] :
                count_so_far += 1
            else:
                count_so_far = 1
            if nums[i + 1] == nums[i] and count_so_far == 3:
                if ans is None:
                    ans = 0
                ans = max(int(nums[i]), ans)
        if ans is None:
            return ""
        return str(ans) * 3
                