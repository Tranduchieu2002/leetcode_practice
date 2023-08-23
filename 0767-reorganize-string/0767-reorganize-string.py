from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        mp = Counter(s)
        mp = sorted(mp.items(), key=lambda pair: pair[1], reverse=True)
        n = len(s)
        if mp[0][1] > (n + 1) // 2:
            return ""
        ans = ["" for _ in range(n)]
        m = len(mp)
        i, j = 0, 0
        while i < len(s):
            while j < m and mp[j][1] == 0:
                j += 1
            if j == m:
                break
            ans[i] = mp[j][0]
            mp[j] = (mp[j][0], mp[j][1] - 1)
            i += 2
        i = 1
        while i < len(s):
            while j < m and mp[j][1] == 0:
                j += 1
            if j == m:
                break
            ans[i] = mp[j][0]
            mp[j] = (mp[j][0], mp[j][1] - 1)
            i += 2
        return "".join(ans)
