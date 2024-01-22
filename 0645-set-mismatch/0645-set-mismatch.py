class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        flags = [-1, -1]
        ans = []
        for i in range(n):
            num = abs(nums[i]) - 1
            
            if nums[num] < 0:
                flags[0] = num + 1
            else:
                nums[num] *= -1
        for i in range(n):
            if nums[i] > 0:
                flags[1] = i + 1
            else:
                nums[i] *= -1
        return flags
    # duplicate 
    #-1, -2, -3, -4, 
    # 1 2 3 4 5 6
    # 1 = 0
    # 2 = -1
    # 2 = <0 => duplicate
    
    