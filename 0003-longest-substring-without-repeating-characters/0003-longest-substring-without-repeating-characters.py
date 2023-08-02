class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left, right = 0, 0
        n = len(s)
        if n <= 2: return len(set(s))
        ans  = 0
        mp = {}
        
        while(right < n):
            curChar = s[right]
            
            if curChar in mp:
                ans = max(ans, right - left)
                left = max(mp[curChar] + 1, left)
                del mp[curChar]
            mp[curChar] = right
            right +=1
            
        return max(ans, right - left)
            
            