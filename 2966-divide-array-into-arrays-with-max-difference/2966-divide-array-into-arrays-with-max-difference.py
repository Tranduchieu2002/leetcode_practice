class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        visited = set()
        n = len(nums)
        for i in range(0, n - 2, 3):
            if nums[i + 2] - nums[i] <= k:
                ans.append([nums[i], nums[i + 1], nums[i + 2]])
            else:
                return []
        return ans