class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        cnt_prev = defaultdict(int)
        n = len(s)
        freq = [0] * 26
        ans  = -1
        for i in range(n):
            c = ord(s[i]) - ord('a')
            freq[c] += 1
            if (freq[c] > 1):
                ans = max(ans, i - 1 - cnt_prev[c])
            if c not in cnt_prev:
                cnt_prev[c] = i
        
        return ans