class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows <= 1): return s
        ans = ""
        col, d = 0 , 1
        i , n = 0, len(s)
        res = ["" for _ in range(numRows)]
        for i in range(n):
            res[col] += s[i]

            if(col == numRows - 1):
                d = 2 - numRows
            if(d <= 0):
                col -= 1
                d += 1
            else: col += 1
        ans = "".join(res)
        return ans
        