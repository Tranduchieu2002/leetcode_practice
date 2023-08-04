class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        m = len(wordDict)
        memo = {}
        def solve(res: str):
            
            if(len(res) == 0): return True
            
            if(res in memo): return memo[res]
            
            for w in wordDict:
                if(res.startswith(w)):
                    if(solve( res[ len(w): ])):
                        memo[res] = True
                        return True
            
            memo[res] = False
            
            return False
        return solve(s)