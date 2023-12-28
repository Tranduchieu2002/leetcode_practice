INF = float('inf')
class Solution:
    
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        @cache
        def solve(i, k, prev, cnt):
            
            if k < 0:
                return INF
            if i >= len(s):
                return 0
            
            delete = solve(i + 1, k - 1, prev, cnt)
            
            ans = 0
            if s[i] == prev:
                over_range = 0
                if cnt in [1, 9, 99]:
                    over_range = 1
                ans = over_range + solve(i + 1, k, prev, cnt + 1)
            else:
                ans = 1 + solve(i + 1, k, s[i], 1)
                
            ans = min(ans, delete)
            return ans
        
        return solve(0, k, None, 0)