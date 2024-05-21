class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def backtrack(i, res):
            ans.append(res[:]) 
            
            for j in range(i, n):
                res.append(nums[j])
                backtrack(j + 1, res)
                res.pop()
            return
        
        backtrack(0, [])
        return ans