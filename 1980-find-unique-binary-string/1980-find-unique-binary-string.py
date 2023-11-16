class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        seen = set()

        for binary_string in nums:
            seen.add(int(binary_string, 2))

        n = len(nums[0])

        for i in range(len(nums) + 1):
            if i not in seen:
                return bin(i)[2:].zfill(n) 
