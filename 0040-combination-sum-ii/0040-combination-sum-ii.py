class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        candidates.sort()
        print(candidates)
        
        def backtrack(start, target, res):
            if target == 0:
                ans.append(res[:])
                return
            
            for i in range(start, len(candidates)):
                print(i, start, res)
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                res.append(candidates[i])
                backtrack(i + 1, target - candidates[i], res)
                res.pop()
        
        ans = []
        backtrack(0, target, [])
        return ans