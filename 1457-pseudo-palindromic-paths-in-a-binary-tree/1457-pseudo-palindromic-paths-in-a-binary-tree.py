# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode], cnt = 0) -> int:
        # count number of elements 
        # => dfs and count number of element
        if root is None:
            return 0
        
        cnt ^= 1 << (root.val - 1)
        
        res = self.pseudoPalindromicPaths(root.left, cnt) + self.pseudoPalindromicPaths(root.right, cnt)
        
        # in postorder when root.left = root.right meaning leftnode is root
        if root.left == root.right:
            if cnt.bit_count() < 2:
                res += 1
        return res