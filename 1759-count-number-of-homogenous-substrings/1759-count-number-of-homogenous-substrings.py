mod = 10 ** 9 + 7
class Solution:
    def countHomogenous(self, s: str) -> int:
        
        ans  = 0
        n =  len(s)
        i = 0
        while i < n:
            cnt = 0
            cur_c = s[i]
            while i < n and cur_c == s[i]:
                i += 1
                cnt += 1
            
            ans = (ans + (cnt * (cnt + 1) % mod ) // 2) % mod
        
        return ans % mod