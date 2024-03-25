class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        ans = set()
        prev = 0
        i = 0
        n = len(nums)
        while i < n:
            val = nums[i]
            temp = i + 1
            while temp < n and  val == nums[temp]:
                temp += 1
                    
            if temp - i - 1 == 1:
                i += (temp - i - 1)
                ans.add(val)
            i += 1
            
        return ans