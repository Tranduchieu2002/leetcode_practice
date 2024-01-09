class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor_array = 0

        # Calculate XOR of all elements in the array
        for num in nums:
            xor_array ^= num

        # Check if XOR of the array is already equal to k
        if xor_array == k:
            return 0

        target_xor = xor_array ^ k

        min_operations = target_xor.bit_count()
        
        return min_operations   