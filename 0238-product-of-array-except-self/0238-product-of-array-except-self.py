class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalMul = 1
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
                continue
            totalMul *= num
        
        ans = []
        for num in nums:
            temp = 0
            if (zeros == 0 or (zeros == 1 and num == 0)):
                temp = totalMul  if num == 0 else totalMul // num
            ans.append(temp)
        return ans