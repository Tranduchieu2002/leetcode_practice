class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)  # sort words by its length
        ans = 0
        dp = defaultdict(int)
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp and dp[word] < dp[predecessor] + 1:
                    dp[word] = dp[predecessor] + 1
            ans = max(ans, dp[word])
        return ans