class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(1, len(points)):
            cur_point = points[i - 1]
            next_point = points[i]
            
            ans += max(abs(cur_point[0] - next_point[0]),abs(cur_point[1] - next_point[1]) )
        return ans