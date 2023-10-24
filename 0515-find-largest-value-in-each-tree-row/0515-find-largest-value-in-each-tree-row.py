min_inf = -float('inf')
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        dq = deque([root])
        ans = []
        while dq:
            max_val  = min_inf
            index_node_row = len(dq)
            for _ in range(index_node_row):
                cur_node  = dq.popleft()
                max_val = max(cur_node.val, max_val)
                # print([cur_node.left, cur_node.right])
                for node  in [cur_node.left, cur_node.right]:
                    if node is None:
                        continue
                    dq.append(node)
            ans.append(max_val)
        
        return ans
        