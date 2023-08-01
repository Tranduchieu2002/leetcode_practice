class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        nums = [0] * (k)
        def solve( pos, curr): 
            if pos == k:
                ans.append(nums[:])
                return;
            for i in range(curr, n-k+pos+2):
                nums[pos] = i
                solve(pos + 1, i + 1)
        solve(0, 1)
        return ans