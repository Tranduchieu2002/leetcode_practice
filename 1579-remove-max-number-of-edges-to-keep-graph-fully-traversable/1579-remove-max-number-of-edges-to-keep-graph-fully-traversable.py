class UnionFind:
    def __init__(self, N):
        self.components = N
        self.parents = list(range(N + 1))
    def union(self, child, parent):
        root_child , root_parent = self.find(child), self.find(parent)
        if root_child == root_parent:
            return 0
        self.parents[root_parent] = root_child
        self.components -= 1
        return 1
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def isConnected(self):
        # thanh phan lien thong ok
        return self.components ==  1
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        reusage_edges = 0
        
        bob, alice = UnionFind(n), UnionFind(n)
        
        for t, u, v in edges:
            if t != 3:
                continue
            reusage_edges += bob.union(u, v) | alice.union(u, v)

        for t, u, v in edges:
            reunsable = 0 
            if t == 1:
                # alice 
                reusage_edges += alice.union(u, v)
            if t == 2:
                # bob
                reusage_edges += bob.union(u, v)
        
        if bob.isConnected() and alice.isConnected():
            return len(edges) - reusage_edges
        return -1
            