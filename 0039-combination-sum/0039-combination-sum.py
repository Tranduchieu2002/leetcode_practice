class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        ans = []
        candidates.sort()
        
        def solve(total, curr, res):
            if total < 0: return
            if total == 0:
                ans.append(res[:])
                return
            
            for i in range(curr, n):
                if (target - candidates[i] < 0 or candidates[i] > target):
                    continue
                res.append(candidates[i])
                solve(total - candidates[i], i, res)
                res.pop()
        solve(target, 0, [])
        return ans
            