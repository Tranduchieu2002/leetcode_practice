mod = 10 ** 9 + 7
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        ans = 0
        dic = defaultdict(int)
        for i, n in enumerate(nums):
            temp = n - (int)(str(n)[::-1])
            ans = (ans % (mod) + dic[temp])
            dic[temp] += 1
        return ans % (mod)