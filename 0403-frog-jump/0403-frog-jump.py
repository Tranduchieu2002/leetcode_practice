class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        max_ele = stones[-1]
        mp = {}
        for i in range(n):
            mp[stones[i]] = i
        @cache
        def dp(i, unit):
            if i >= n or unit > n:
                return False
            if i == n - 1:
                return True
            cur_state = stones[i]
            
            ans = False
            for j in range(unit - 1, unit + 2):
                next_state = cur_state + j
                if next_state in mp and mp[next_state] > i:
                    if dp(mp[next_state], j):
                        ans = True
            
            return ans
        return dp(stones[0], 0)