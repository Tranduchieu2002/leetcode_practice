class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        numsOfItemNeeded = n // 3
        dict = defaultdict(int)
        for val in nums:
            dict[val] += 1
        
        ans = []
        for key in dict:
            if dict[key] > numsOfItemNeeded:
                ans.append(key)
        
        return ans