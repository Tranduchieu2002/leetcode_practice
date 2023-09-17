class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q , seen = deque(), set()
#       q including (cur node , dist, mask) and seen including (node, mask)
        maskAllPaths = (1 << n) - 1
        for i in range(n):
            q.append((i, 0, 1 << i))
        while q:
            cur_node, dist, mask = q.popleft()
            if mask == maskAllPaths:
                return dist
            
            for neighbor in (graph[cur_node]):
                next_mask = mask | ( 1 << neighbor )
                if (neighbor, next_mask) not in seen:
                    seen.add((neighbor, next_mask))
                    q.append((neighbor, dist + 1, next_mask))
            
         # Node with mask off thiss node 
        return 0