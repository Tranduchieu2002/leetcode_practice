class Solution:
    # def topo_sort(self)
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        m = len(edges)
        q = deque()
        adj = [[] for _ in range(n)]        
        in_deg = [0] * n
        for (u, v) in edges:
            adj[u].append(v)
            adj[v].append(u)
            in_deg[u] += 1
            in_deg[v] += 1
        for i, node in enumerate(in_deg):
            if not hasApple[i] and in_deg[i] == 1:
                q.append(i)
        ans = 0
        while(q):
            u = q.popleft()
            if u == 0:
                continue
            for v in adj[u]:
                in_deg[v] -= 1
                ans += 1
                adj[v].remove(u)
                if (in_deg[v] == 1 and not hasApple[v]):
                    q.append(v)
        return  (n - 1 - ans) * 2