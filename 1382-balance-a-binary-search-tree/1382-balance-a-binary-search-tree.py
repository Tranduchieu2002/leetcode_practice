# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            nodes.append(root.val)
            print(root.val)
            inorder(root.right)
        inorder(root)
        def balancedBST(l, r):
            if l > r:
                return
            m = l + (r - l) // 2
            
            node_l, node_r = balancedBST(l, m - 1), balancedBST(m + 1, r)
            return TreeNode(nodes[m], node_l, node_r)
        return balancedBST(0, len(nodes) - 1)