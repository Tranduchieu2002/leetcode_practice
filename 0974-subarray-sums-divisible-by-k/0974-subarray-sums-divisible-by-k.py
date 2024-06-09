
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixMod = 0
        result = 0
        # There are k mod groups 0...k-1.
        modGroups = [0] * k
        modGroups[0] = 1

        for num in nums:
            prefixMod = (prefixMod + num % k + k) % k
            result += modGroups[prefixMod]
            modGroups[prefixMod] += 1

        return result
