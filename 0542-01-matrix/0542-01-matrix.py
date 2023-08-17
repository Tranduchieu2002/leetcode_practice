class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n , m =  len(mat), len(mat[0])
        ans = [[0] * m for _ in range(n)]
        q = deque()
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j))
    
        count = 0
        while q:
            count += 1
            k = len(q)
            while k > 0:
                k -= 1
                start_point = q.popleft()
                for (x , y) in d:
                    dx = start_point[0] + x
                    dy = start_point[1] + y
                    
                    if dx < 0 or dx == n or dy < 0 or dy == m or mat[dx][dy] == 0:
                        continue
                    ans[dx][dy] = count
                    q.append((dx, dy))
                    mat[dx][dy] = 0
            
        return ans