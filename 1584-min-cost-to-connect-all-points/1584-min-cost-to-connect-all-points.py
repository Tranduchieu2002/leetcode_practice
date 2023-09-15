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
        if (p_u == p_v):
            return False
        self.parent[p_v] = p_u
        return True
class Solution:
    def findDistance(self, a: list,b: list):
        x_a, y_a = a
        x_b, y_b = b
        return abs(x_a - x_b) + abs(y_a - y_b)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = []
        n , ans= len(points), 0
        count_connected_point = 0
        for i in range(n):
            for j in range(i + 1, n):
                graph.append((i, j, self.findDistance(points[i], points[j])))
        uf = Union_Find(n)
        graph = sorted(graph, key= lambda x: x[2])
        for edge in graph:
            (u, v, w) = edge
            if uf.union(u,v):
                count_connected_point += 1
                ans += w
            if count_connected_point == n:
                break
        return ans
        