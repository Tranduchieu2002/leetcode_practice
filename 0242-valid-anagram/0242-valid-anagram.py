class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        freq = [0] * 26
        
        def charToInt(c1):
            return ord(c1) - ord('a')
        for i in range(len(s)):
            freq[charToInt(s[i])] += 1
            freq[charToInt(t[i])] -= 1
        k = 0
        print(freq)
        while k < len(freq) and freq[k] == 0:
            k += 1
        return k == 26