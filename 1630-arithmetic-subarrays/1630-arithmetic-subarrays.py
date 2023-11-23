class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(nums)
        m = len(l)
        ans = [True] * m
        for i in range(m):
            left_q, right_q = l[i], r[i]
            len_sub = right_q - left_q
            temp_arr = sorted(nums[left_q: (left_q + len_sub + 1)])
            val = temp_arr[1] - temp_arr[0]
            for j in range(1, len(temp_arr)):
                if(temp_arr[j] - temp_arr[j - 1] != val):
                    ans[i] = False
                    break;
        
        return ans
            