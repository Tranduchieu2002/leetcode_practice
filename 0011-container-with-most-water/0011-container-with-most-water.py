class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        low, high = 0 , n - 1
        ans = 0
        while(low <= high):
            area = min(height[low], height[high]) * abs(high - low)
            ans = max(ans, area)                      
            if height[low] < height[high]:
                low += 1
            else :
                high -= 1
        return ans