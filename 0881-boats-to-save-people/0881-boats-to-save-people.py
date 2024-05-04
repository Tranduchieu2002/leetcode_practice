class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        p.sort()
        ans= 0
        l, r=0, len(p)-1
        while l<=r:
            
            ans+=1
            if p[l]+p[r]<=limit:
                l+=1
            r-=1
        return ans