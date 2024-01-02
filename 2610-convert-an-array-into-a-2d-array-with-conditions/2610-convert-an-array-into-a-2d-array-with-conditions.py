class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        n = len(nums)
        freq = defaultdict(int)
        for i in range(n):
            freq[nums[i]] += 1
        
        while max(freq.values())  > 0:
            temp = []
            
            for key in freq:
                if freq[key] > 0:
                    temp.append(key)
                freq[key] -= 1
                
            ans.append(temp)
        
        return ans