class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        ans = 0
        n = len(colors)
        ans += colors[-1] != colors[0] and colors[1] != colors[0]
        ans += colors[-2] != colors[-1] and colors[-1] != colors[0]
        for i in range(1, n - 1):
            ans += bool(colors[i - 1] != colors[i] and colors[i + 1] != colors[i])
            
        return ans