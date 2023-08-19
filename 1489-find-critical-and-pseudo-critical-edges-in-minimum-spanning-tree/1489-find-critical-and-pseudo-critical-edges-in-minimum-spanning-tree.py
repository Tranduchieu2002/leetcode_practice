class Union_Find:
    def __init__(self, n):
        self.parent = list(range(n))
        
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] =  self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        self.parent[root_x] = self.parent[root_y]
        
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:        
        critical = []
        pseudo_critical = []
        copied_edges = [edge.copy() for edge in edges]
        
        def mst(edges, block, e):
            weight = 0
            uf = Union_Find(n)
            if e != -1:
                uf.union(edges[e][0], edges[e][1]) 
                weight += edges[e][2]
            for i, edge in enumerate(copied_edges):
                if i == block:
                    continue
                if uf.find(edge[0]) == uf.find(edge[1]):
                    continue
                uf.union(edge[0], edge[1])
                # print(uf.parent, edge[0], edge[1])                
                weight += edge[2]
#               trunfg dinh
            for i in range(n):
                if uf.find(i) != uf.find(0):
                    return float('inf')
            print(uf.parent, e , block)
            return weight
        
        for (i, edge) in enumerate(edges):
            
            copied_edge = edge
            copied_edge.append(i)
            copied_edges[i] = copied_edge
        # edges.sort(key=lambda x: x[2])
        copied_edges.sort(key=lambda x: x[2])    
        m_w = mst(copied_edges,- 1, -1)
        for i, edge in enumerate(copied_edges):
#              if we ignore critical edge we got mst greater than min 
            if  m_w < mst(copied_edges, i, -1):
                critical.append(edge[3])
            elif m_w == mst(copied_edges, -1, i):
                pseudo_critical.append(edge[3])
                
        return [critical, pseudo_critical]
    
            
        
        