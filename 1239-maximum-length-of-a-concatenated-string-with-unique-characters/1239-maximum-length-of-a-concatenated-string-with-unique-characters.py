class Solution:
    def make_unique(self, words):
        unique_words = []
        for word in words:
            unique_chars = []
            for char in word:
                if char not in unique_chars:
                    unique_chars.append(char)
            unique_words.append("".join(unique_chars))
        return unique_words
        
    def maxLength(self, arr: List[str]) -> int:
        # unique_words = self.make_unique(arr)
        # print(unique_words)
        dp = {0: 0}
        for w in (arr):
            if len(set(w)) != len(w): continue
            for k in list(dp.keys()):
                newMask = k
                isValid = all(not newMask & 1 << (ord(c) - ord('a')) for c in w)
                if isValid:
                    for c in w:        
                        newMask |= 1 << (ord(c) - ord('a'))

                    dp[newMask] = max(dp[k] + len(w), dp.get(newMask, 0))
        return max(dp.values())
        
            