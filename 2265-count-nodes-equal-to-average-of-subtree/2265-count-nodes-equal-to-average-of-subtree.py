# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        
        def solve(root):
            nonlocal ans
            if root is None:
                return [0, 0]
            
            left_avg = solve(root.left)
            right_avg = solve(root.right)
            
            sum_a = root.val + left_avg[0] + right_avg[0]
            len_a = 1 + left_avg[1] + right_avg[1]
            
            avg = sum_a // len_a
            if avg == root.val:
                ans += 1            
            # return sum and len node
            return [sum_a, len_a]
    
        solve(root)
        return ans