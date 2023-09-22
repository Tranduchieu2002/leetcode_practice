class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n , m = len(t), len(s)
        j = 0
        for i in range(n):
            if j >= m:
                break
            if s[j] == t[i]:
                j += 1
        return j == m