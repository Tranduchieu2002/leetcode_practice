class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        min_val = float('inf')
        
        st = []
        
        for val in nums:
            
            while st and st[-1][0] < val:
                st.pop()
            
            if st and st[-1][1] < val and st[-1][0] > val:
                return True
            
            min_val = min(min_val, val)
            st.append((val, min_val))
        
        return False
                
                