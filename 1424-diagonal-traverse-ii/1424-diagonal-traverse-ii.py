class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        dic = defaultdict(list)
        
        rows = len(nums)
        cols = 0
        max_n = rows
        n = len(nums)
        for i in range(rows):
            max_n += len(nums[i])
            for j in range(len(nums[i])):
                dic[i + j].append(nums[i][j])
        
        for k in dic:
            while dic[k]:
                ans.append(dic[k].pop())
            
        return ans
                