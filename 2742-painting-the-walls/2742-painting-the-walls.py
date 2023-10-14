inf = float('inf')
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        
        n = len(time)
        @cache
        def solve(i , wallsRemain):
            if wallsRemain <= 0:
                return 0
            
            if i >= n:
                return inf
            
            take = cost[i] + solve(i + 1, wallsRemain - time[i] - 1)
            notTake = solve(i + 1, wallsRemain)
            
            return min(take, notTake)
        
        return solve(0, n)
            
            
            