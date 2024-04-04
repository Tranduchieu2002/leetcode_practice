class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        depth = 0
        for  c in s:
            if c == '(':
                ans += 1
            
            if c == ')':
                depth = max(depth, ans)
                ans -= 1
        return depth