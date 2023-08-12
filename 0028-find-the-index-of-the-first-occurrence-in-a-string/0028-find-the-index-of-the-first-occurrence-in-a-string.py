class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        
        idx = 0;
        i = 0
        while(i < n):
            
            if haystack[i] == needle[idx]:
                idx += 1
                i += 1
            else:
                i = i - idx + 1
                idx = 0
                
            if idx == m:
                return i - idx
        return -1
                
            
                
            
            
            
            
        