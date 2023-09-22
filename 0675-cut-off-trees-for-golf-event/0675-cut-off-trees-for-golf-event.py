from collections import deque, defaultdict

class Solution:
    def cutOffTree(self, forest) -> int:
        # Define possible movement directions (up, down, left, right)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        n, m = len(forest), len(forest[0])

        def notValidPaths(i, j):
            return i < 0 or i >= n or j < 0 or j >= m or forest[i][j] == 0

        def bfs(start, target):
            q = deque()
            q.append(start)
            distance = defaultdict(int)
            visited = set()
            visited.add(start)

            while q:
                size = len(q)
                for _ in range(size):
                    x, y = q.popleft()
                    if (x, y) == target:
                        return distance[target]

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if (nx, ny) in visited or notValidPaths(nx, ny):
                            continue
                        distance[(nx, ny)] = distance[(x, y)] + 1
                        q.append((nx, ny))
                        visited.add((nx, ny))

            return -1

        trees = []
        for i in range(n):
            for j in range(m):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))
        trees.sort()
        
        ans = 0
        start = (0, 0)
        for _, i, j in trees:
            dist = bfs(start, (i, j))
            if dist == -1:
                return -1
            ans += dist
            start = (i, j)
        return ans
