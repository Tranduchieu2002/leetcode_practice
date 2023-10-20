# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.ans = []
        def flatten(arr):
            result = []
            for num in arr:
                if num.isInteger():
                    result.append(num.getInteger())
                else:
                    result.extend(flatten(num.getList()))
            return result
        self.ans = flatten(nestedList)
        self.i = 0
        self.len = len(self.ans)
    
    def next(self) -> int:
        if (not self.hasNext()):
            return -1
        
        cur = self.ans[self.i]
        self.i += 1
        return cur
    
    def hasNext(self) -> bool:
        return self.i < self.len
             
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())