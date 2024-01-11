# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root, min_val, max_val):
            nonlocal ans
            if root is None:
                return
            ans = max(ans, abs(max_val - root.val), abs(min_val - root.val))
            
            min_val = min(min_val, root.val)
            max_val = max(max_val, root.val)
            dfs(root.left, min_val, max_val)
            dfs(root.right,min_val, max_val)
        
        dfs(root,root.val, root.val)
        return ans