class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = [0,0]
        temp = 0
        
        for val in range(len(nums)):
            temp ^= nums[val]
        flag = 0
        while temp >> flag & 1 == 0:
            flag += 1
        for num in nums:
            if (num >> flag & 1) == 1:
                ans[0] ^= num
            else:
                ans[1] ^= num
        return ans