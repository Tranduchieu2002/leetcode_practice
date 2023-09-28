class Solution:
    def __init__(self):
        self.ans = []
    def isPalindrome(self, s, start, end):
        while start <= end:
            if  not s[start] == s[end]:
                return False
            start += 1
            end -= 1
        return True
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        def backtrack(curIndex:int, res: list[str]):
            if curIndex == n:
                self.ans.append(res[:])
                return
            
            for i in range(curIndex, n):
                if self.isPalindrome(s, curIndex, i):
                    res.append(s[curIndex: i + 1])
                    backtrack(i + 1, res)
                    res.pop()
            
        backtrack(0, [])
        return self.ans