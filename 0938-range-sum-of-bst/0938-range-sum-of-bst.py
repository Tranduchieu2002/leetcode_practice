# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = 0
        self.low, self.high = 0, 0

    def dfs(self, root):
        if root is None:
            return 0

        left_sum = self.dfs(root.left)
        right_sum = self.dfs(root.right)

        if self.low <= root.val <= self.high:
            return root.val + left_sum + right_sum
        else:
            return left_sum + right_sum

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.low = low
        self.high = high
        return self.dfs(root)
