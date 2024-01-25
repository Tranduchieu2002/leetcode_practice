class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s1, s2 = text1, text2
        l1, l2 = len(text1), len(text2)
        row, col = l1+1, l2+1
        
        if not l1 or not l2:
            return 0
        
        memo = [0 for _ in range(col)]
        
        for r in range(1, row):
            # use prev to keep memo[r-1][c-1]
            prev = memo[0]
            for c in range(1, col):
                tmp = memo[c] 
                if s1[r-1] == s2[c-1]:
                    memo[c] = prev + 1
                else:
                    memo[c] = max(memo[c-1], memo[c])
                prev = tmp
            
        return memo[-1]