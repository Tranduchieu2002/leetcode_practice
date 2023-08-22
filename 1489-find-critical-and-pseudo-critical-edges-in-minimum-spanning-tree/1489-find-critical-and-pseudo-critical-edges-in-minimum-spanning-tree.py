class Solution:
    class Union_Find():
        def __init__(self, n):
            self.parent = list(range(n))
        def find(self, u):
            parent = self.parent
            if parent[u] != u:
                parent[u] = self.find(parent[u])
            return parent[u]
        def union(self, u, v):
            p_u = self.find(u)
            p_v = self.find(v)
            if (p_u != p_v):
                self.parent[p_v] = p_u
        
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        m = len(edges)
        critical = []
        pseudo_critical = []
        for i in range(m):
            edges[i].append(i)
        
        edges.sort(key = lambda x:x[2])
        
        def mst(take = -1, rm = -1):
            
            uf = self.Union_Find(n)
            weight = 0
            if take != -1:
                uf.union(edges[take][0],edges[take][1])
                weight += edges[take][2]
            for (i , edge) in enumerate(edges):
                (u, v, w, j) = edge
                if uf.find(u) != uf.find(v):
                    if rm == i:
                        continue
                    uf.union(u, v)
                    weight += w
            for i in range(n): # check is disconnected
                if uf.find(i) != uf.find(0):
                    return 100000
            return weight
        min_cost = mst()
        for (i, edge) in enumerate(edges):
            if mst(-1, i) > min_cost:
                critical.append(edge[3])
            elif mst(i, -1) == min_cost:
                pseudo_critical.append(edge[3])
        return [critical, pseudo_critical]
            
        