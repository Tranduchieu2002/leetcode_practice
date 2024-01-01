class Solution:
    def findContentChildren(self, g: List[int], cookies: List[int]) -> int:
        
        g.sort()
        cookies.sort()
        n, m = len(g), len(cookies)
        i , j = 0, 0
        while i < n and  j < m:
            if g[i] <= cookies[j]: # cangive for child
                j += 1
                i += 1
            else:
                j += 1
        return i