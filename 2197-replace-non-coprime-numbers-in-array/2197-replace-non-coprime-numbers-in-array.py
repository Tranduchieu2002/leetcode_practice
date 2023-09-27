class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        st = []
        n = len(nums)
        for i in range(n):
            st.append(nums[i])
            while len(st) > 1 and gcd(st[-1], st[-2]) > 1:
                
                gcd1 =  gcd(st[-1], st[-2])
                lcm1 = (st.pop() * st.pop()) // gcd1
                
                st.append(lcm1)
            
        return st