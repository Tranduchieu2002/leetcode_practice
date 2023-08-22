class Solution:
    def to_string(self, number):
        return chr(number + ord('A'))
    def convertToTitle(self, columnNumber: int) -> str:
        mod = 26 
        ans = ""
        while columnNumber > 0:
            t = (columnNumber + 25) % mod
            ans = self.to_string(t) + ans
            columnNumber = ((columnNumber - 1) // 26)
        return ans