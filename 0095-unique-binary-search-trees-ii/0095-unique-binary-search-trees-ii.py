# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        memo = {}
        
        def generateTree(start, end):
            # if(start == 0):
            #     return []
            if f"{start}-{end}" in memo:
                return memo[f"{start}-{end}"]
            
            ans = []            
            if(start > end):
                ans.append(None)
                return ans
            
            for rootVal in range(start, end + 1):
                leftNodes = generateTree( start, rootVal - 1)
                rightNodes = generateTree(rootVal + 1, end)
                for leftNode in leftNodes:
                    for rightNode in rightNodes:
                        root =  TreeNode(rootVal, leftNode, rightNode) 
                        ans.append(root)
            
            memo[f"{start}-{end}"] = ans
            
            return ans
        return generateTree(1, n)