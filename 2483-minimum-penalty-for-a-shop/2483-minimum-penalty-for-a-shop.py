class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        ans = 0
        cur_p = p = 0
        for i in range(n):
            c = customers[i]
            cur_p += 1 if c == 'N' else -1
            if cur_p < p:
                p = cur_p
                ans = i + 1
        return ans