# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseTree(self, level, left, right):
        if left is None or right is None:
            return
        if level % 2 == 1:
            left.val, right.val = right.val, left.val
        self.reverseTree(level + 1, left.left, right.right)
        self.reverseTree(level + 1, right.left, left.right)
        
        return 
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        left, right = root.left, root.right
        self.reverseTree(1, left, right)
    
        return root
        
        