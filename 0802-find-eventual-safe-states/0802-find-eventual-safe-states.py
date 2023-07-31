class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = {}  # Initialize an empty adjacency list
        dis = [0] * n
        q = [] # queue
        for i in range(n):
            adj[i] = []

        # Append neighbors to the adjacency list
        for i, val in enumerate(graph):
            for neighbor in val:
                dis[i] = dis[i] + 1
                adj[neighbor].append(i)
        for i, val in enumerate(dis):
            if(val == 0): q.append(i)
        ans = []
        while q:
            top = q.pop()
            ans.append(top)
            
            for val in adj[top]:
                dis[val] -= 1;
                if(dis[val] == 0): 
                    q.append(val)
        ans.sort()
        return ans
