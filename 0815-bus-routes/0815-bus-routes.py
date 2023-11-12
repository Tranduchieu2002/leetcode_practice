class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        adj = defaultdict(list)
        n = len(routes)
        for i in range(n):
            for route  in routes[i]:
                adj[route].append(i)
        
        q = [source]
        visited = [False] * (n + 1)
        ans = 0
        
        while q:
            size = len(q)
            while size > 0:
                top = q.pop(0)
                
                if top == target:
                    return ans
                
                for nei in adj[top]:
                    
                    if (visited[nei]):
                        continue
                    visited[nei] = True
                    
                    for route in routes[nei]:
                        q.append(route)
                size -= 1
            
            ans += 1
        return -1
        