# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        number_freq = defaultdict(int)
        def findNum(node):
            if node is None:
                return;
            findNum(node.left)
            
            number_freq[node.val] += 1
            
            findNum(node.right)
        findNum(root)
        max_freq = 0
        nums = []
        for key in number_freq:
            if number_freq[key] >= max_freq:
                max_freq =  number_freq[key]
        for key in number_freq:  
            if number_freq[key] == max_freq:
                nums.append(key)
        return nums
        