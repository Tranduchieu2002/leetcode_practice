# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        adj = defaultdict(list)
        visited = set([start])
        def dfs(root, parent = None):
            if root is None:
                return []
                        
            adj[root.val].extend(dfs(root.left, root.val) + dfs(root.right, root.val))
            if parent is not None:
                adj[root.val].append(parent)
            return [root.val]
        
        dfs(root, None)
        if start not in adj:
            return 0
        ans = 0
        removes = adj[start]
        
        total = len(adj)
        while removes:
            ans += 1
            temp = removes
            removes = []
            for val in temp:
                if val in visited:
                    continue
                visited.add(val)
                for nei in adj[val]:
                    if nei in visited:
                        continue
                    removes.append(nei)
        return ans
            