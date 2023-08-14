class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        
        ans = False
        adj = [[] for _ in range(n)]
        visited = [False] * n
        detect = [False] * n        
        for i in range(len(p)):
            adj[p[i][0]].append(p[i][1])
            
        def dfs(i):
            visited[i] = True
            detect[i] = True
            neighbors = adj[i]
            for neighbor in neighbors:
                if detect[neighbor]:
                    return True
                if not visited[neighbor] and  dfs(neighbor):
                    return True
            detect[i] = False
            return False
        for i in range(n):
            if not visited[i] and dfs(i):
                return False
            
        return True