# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def postTraversal(root):
            if not root:
                return
            
            postTraversal(root.left)
            postTraversal(root.right)
            ans.append(root.val)
        postTraversal(root)
        return ans