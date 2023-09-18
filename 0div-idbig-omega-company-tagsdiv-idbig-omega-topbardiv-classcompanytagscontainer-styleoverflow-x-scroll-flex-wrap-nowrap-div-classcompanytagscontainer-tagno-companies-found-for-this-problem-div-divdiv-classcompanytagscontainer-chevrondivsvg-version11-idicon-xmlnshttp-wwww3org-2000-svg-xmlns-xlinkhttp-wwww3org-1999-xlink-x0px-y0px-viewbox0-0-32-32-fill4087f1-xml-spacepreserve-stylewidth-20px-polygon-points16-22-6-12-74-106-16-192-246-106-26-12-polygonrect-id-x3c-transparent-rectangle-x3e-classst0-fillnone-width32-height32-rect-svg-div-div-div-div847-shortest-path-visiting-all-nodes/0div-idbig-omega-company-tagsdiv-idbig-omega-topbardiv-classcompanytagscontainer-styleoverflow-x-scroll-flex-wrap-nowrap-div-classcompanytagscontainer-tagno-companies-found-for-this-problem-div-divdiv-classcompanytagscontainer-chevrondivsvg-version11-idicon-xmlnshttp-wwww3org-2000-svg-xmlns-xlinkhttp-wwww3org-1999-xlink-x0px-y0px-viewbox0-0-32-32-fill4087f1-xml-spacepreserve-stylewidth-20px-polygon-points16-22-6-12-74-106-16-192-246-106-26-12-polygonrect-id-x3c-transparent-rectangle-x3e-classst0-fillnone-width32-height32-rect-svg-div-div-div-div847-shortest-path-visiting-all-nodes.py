class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q , seen = [], set()
#       q including (cur node , dist, mask) and seen including (node, mask)
        maskAllPaths = (1 << n) - 1
        dist = 0
        for i in range(n):
            q.append((i, 1 << i))
            seen.add((i, 1 << i))
        while q:
            dist += 1
            new_state_q = []
            for cur_node, mask in q:
                for neighbor in (graph[cur_node]):
                    next_mask = mask | ( 1 << neighbor)
                    if next_mask == maskAllPaths:
                        return dist
                    if (neighbor, next_mask) not in seen:
                        seen.add((neighbor, next_mask))
                        new_state_q.append((neighbor, next_mask))
            q = new_state_q
         # Node with mask off thiss node 
        return 0