class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        completed = time//(n-1)
        remaining = time%(n-1)
        ans = 0
        if (completed % 2!= 0):
            ans = n - remaining
        else:
            ans = remaining + 1
        
        return ans