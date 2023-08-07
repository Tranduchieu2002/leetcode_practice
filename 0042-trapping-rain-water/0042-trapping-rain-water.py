class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if(n < 2): return 0
        low, high = 0, n - 1
        ans = 0
        max_low, max_high = height[0], height[-1]
        while(low <= high):
            
            val_low = height[low]
            val_high = height[high]
            print(ans)
            max_low = max(max_low, val_low)
            max_high = max(max_high, val_high)
            
            ans += min(max_low, max_high) - min(val_low, val_high)
            
            if(val_low < val_high): 
                low +=1
            else:
                high -= 1
        print('end')
        return ans
            
            
            
            