class Solution:
    def maxScore(self, s: str) -> int:
        
        cnt_ones, cnt_zeros = s.count('1'), 0
        n = len(s)
        ans = 0
        for i in range(n - 1):
            if s[i] == '0':
                cnt_zeros += 1
            else:
                cnt_ones -= 1
            ans  = max(ans, (cnt_zeros + cnt_ones))
        
        return ans