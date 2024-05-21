class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def checkbit(parent, sub):
            return (parent >> sub) & 1 == 1
        for i in range(1 << n):
            temp = []
            for j in range(n):
                if checkbit(i, j):
                    temp.append(nums[j])
            ans.append(temp)
        return ans