from collections import defaultdict

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        adj = defaultdict(list)
        n = len(routes)

        # Build adjacency list
        for i in range(n):
            for stop in routes[i]:
                adj[stop].append(i)

        q = [source]
        visited = [False] * n  # Use n instead of (n + 1)
        ans = 0

        while q:
            size = len(q)
            while size > 0:
                current_stop = q.pop(0)
                for route in adj[current_stop]:
                    if visited[route]:
                        continue

                    visited[route] = True
                    for next_stop in routes[route]:
                        if next_stop == target:
                            return ans + 1
                        q.append(next_stop)

                size -= 1
            ans += 1

        return -1  # No valid route found
