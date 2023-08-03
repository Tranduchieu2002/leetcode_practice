class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        n = len(digits)
        mp = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        ans = []
        print("234"[1:])
        def backtrack(curr, res):
            if((len(res)) == n):
                ans.append(res[:])
                return
            for c in mp[curr[0]]:
                backtrack(curr[1:], res + c)
                
        backtrack(digits, "")
        return ans