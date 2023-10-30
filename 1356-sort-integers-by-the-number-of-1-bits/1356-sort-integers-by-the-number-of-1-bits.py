from functools import cmp_to_key

class Solution:
    def sortByBits(self, arr):
        def count_set_bits(num):
            return bin(num).count('1')

        def custom_sort(a, b):
            if count_set_bits(a) == count_set_bits(b):
                return a - b
            return count_set_bits(a) - count_set_bits(b)

        sorted_arr = sorted(arr, key=cmp_to_key(custom_sort))
        return sorted_arr
