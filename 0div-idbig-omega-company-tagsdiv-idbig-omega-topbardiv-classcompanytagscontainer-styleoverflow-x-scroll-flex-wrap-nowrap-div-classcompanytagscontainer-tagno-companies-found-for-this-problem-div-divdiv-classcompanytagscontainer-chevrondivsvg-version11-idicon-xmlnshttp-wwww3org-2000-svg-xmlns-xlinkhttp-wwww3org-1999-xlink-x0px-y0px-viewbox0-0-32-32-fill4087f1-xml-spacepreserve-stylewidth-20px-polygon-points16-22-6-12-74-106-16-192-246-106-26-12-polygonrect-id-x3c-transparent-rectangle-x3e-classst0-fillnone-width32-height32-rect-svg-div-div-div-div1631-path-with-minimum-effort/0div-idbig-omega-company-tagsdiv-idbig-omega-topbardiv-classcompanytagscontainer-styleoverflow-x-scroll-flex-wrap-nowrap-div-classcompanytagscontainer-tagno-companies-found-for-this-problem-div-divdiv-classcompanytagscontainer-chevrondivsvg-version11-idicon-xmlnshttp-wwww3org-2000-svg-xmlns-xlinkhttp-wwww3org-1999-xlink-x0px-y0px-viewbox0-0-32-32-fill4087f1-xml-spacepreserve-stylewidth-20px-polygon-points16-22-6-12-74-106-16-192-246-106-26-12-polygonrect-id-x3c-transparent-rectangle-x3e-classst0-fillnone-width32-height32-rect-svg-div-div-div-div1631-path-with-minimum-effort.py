INF = float('inf')

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ans = 0
        d = [[0,0, -1, 1], [1,-1, 0, 0]]
        n, m = len(heights), len(heights[0])
        dist = [[INF] * m for _ in range(n)]
        pq = [(0, 0 , 0)]
        dist[0][0] = 0
        while pq:
            cur_w, cur_row, cur_col = heapq.heappop(pq)
            if cur_row == n - 1 and cur_col == m - 1:
                return cur_w
            for i in range(4):
                dx, dy = cur_row + d[0][i], cur_col + d[1][i]
                if dx < 0 or dx >= n or dy < 0 or dy >= m:
                    continue
                min_cost = max(cur_w, abs(heights[dx][dy] - heights[cur_row][cur_col])) 
                if dist[dx][dy] > min_cost:
                    heapq.heappush(pq, (min_cost, dx, dy))
                    dist[dx][dy] =  min_cost
        return 0