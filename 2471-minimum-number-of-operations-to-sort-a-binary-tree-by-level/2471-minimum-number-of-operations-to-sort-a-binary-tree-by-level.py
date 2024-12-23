# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        result = 0
        q = [root]
        while q:
            qq = [node.val for node in q]
            qqSorted = sorted(qq)
            numToInd = {num: i for i, num in enumerate(qq)}
            for i in range(len(qq)):
                if qq[i] != qqSorted[i]:
                    j = numToInd[qqSorted[i]]
                    qq[j] = qq[i]
                    numToInd[qq[i]] = j
                    result += 1

            qq = []
            for node in q:
                if node.left:
                    qq.append(node.left)
                if node.right:
                    qq.append(node.right)

            q = qq

        return result