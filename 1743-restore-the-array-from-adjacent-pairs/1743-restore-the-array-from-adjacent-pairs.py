class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        
        for u,v in adjacentPairs:
            adj[u].append(v)
            adj[v].append(u)
        root = 0
        for k in adj:
            if (len(adj[k]) == 1):
                root = k
                break
        ans = []
        limit = 10 ** 5 + 1
        visited = {}
        def dfs(curNode):
            if curNode in visited:
                return
            visited[curNode] = True
            ans.append(curNode)
            for nei in adj[curNode]:
                dfs(nei)
        dfs(root)
        return ans
        