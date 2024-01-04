class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counters = defaultdict(int)
        for val in nums:
            counters[val] += 1
        ans = 0
        for key in counters:
            
            need = counters[key]
            if need == 1:
                return -1
            
            ans +=  need // 3 + 1 if need % 3 else need // 3
        
        return ans
                
        