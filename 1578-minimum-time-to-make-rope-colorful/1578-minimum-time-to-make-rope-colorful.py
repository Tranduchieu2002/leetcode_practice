class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        n = len(colors)
        for i in range(1, n):
            if colors[i - 1] == colors[i]:
                ans += min(neededTime[i], neededTime[i - 1])
                # update max in prev time 
                neededTime[i] = max(neededTime[i - 1], neededTime[i])
        
        return ans
            
            
            