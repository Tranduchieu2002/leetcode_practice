class Solution:
    def totalMoney(self, n: int) -> int:
        m, a = n // 7, n % 7
        ans = m * 28 + (m * (m - 1) // 2) * 7
        ans += (a * (a + 1) // 2)
        ans += (a * m)
        
        return ans
                
            
        