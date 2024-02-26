# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        flag = True
        if (p is None and q):
            return False
        if (p and q is None):
            return False
        if (p is None and q is None):
            return True
        
        
        if p.val == q.val:
            flag = flag and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            flag = False
        return flag