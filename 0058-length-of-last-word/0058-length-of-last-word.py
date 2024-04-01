class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        ans = 0
        isWord = False
        
        while s[n - 1] == ' '  and not isWord:
            if (s[n - 1] != ' '):
                isWord = True
            n -= 1
        while n > 0 and s[n - 1] != ' ':
            n -= 1
            ans += 1
        
        return ans