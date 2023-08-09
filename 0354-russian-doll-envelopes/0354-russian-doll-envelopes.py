class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        print(envelopes)
        dp = []
        ans = 0
        for w, h in envelopes:
            if not dp or dp[-1] < h:
                dp.append(h)
                ans += 1
            else:
                idx = bisect_left(dp, h)
                dp[idx] = h
        return len(dp)