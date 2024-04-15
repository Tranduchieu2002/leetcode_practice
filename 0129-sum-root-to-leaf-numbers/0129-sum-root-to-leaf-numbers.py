# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, cur):
        if (not root):
            return 0
        t = cur * 10 + root.val
        if not root.left and not root.right:
            return t
        return self.dfs(root.left, t) + self.dfs(root.right, t)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)