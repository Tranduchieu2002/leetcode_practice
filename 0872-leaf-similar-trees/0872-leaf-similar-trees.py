# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, target):
        
        if root.left is None and root.right is None:
            target.append(root.val)
        if root.left is not None:
            self.dfs(root.left, target)
        
        if root.right is not None:
            self.dfs(root.right, target)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        first_tree = []
        self.dfs(root1,first_tree)
        second_tree = []
        self.dfs(root2, second_tree)
        return first_tree == second_tree
            