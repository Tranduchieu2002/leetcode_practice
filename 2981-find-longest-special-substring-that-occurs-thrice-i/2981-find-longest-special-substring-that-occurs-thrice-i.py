class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        freq = defaultdict(int)       
        ans = 0
        for i in range(n):
            init = s[i]
            cnt  = 0
            for j in range(i, n):
                if s[j] != init:
                    break
                freq[init * (j - i + 1)] += 1
        for key in freq:
            if freq[key] >= 3 and len(key) > ans:
                ans = max(ans, len(key))
        return ans if ans > 0 else -1