INF = float('inf')
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        def findMinSteps(current, copyLength):
            if current == n:
                return 0
            if current > n:
                return INF
            ans = INF
            # normal paste
            normal = 1 + findMinSteps(current + copyLength, copyLength)
            copyAndPaste = 2 + findMinSteps(current * 2, current)
            return min(normal, copyAndPaste)
        return findMinSteps(1,1) + 1