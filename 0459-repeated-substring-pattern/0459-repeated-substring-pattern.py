class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        return s in s[1:] + s[:-1]