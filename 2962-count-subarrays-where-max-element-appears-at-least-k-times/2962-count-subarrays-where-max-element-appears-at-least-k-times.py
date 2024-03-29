class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        start, cnt, maxInSub = 0, 0, 0
        ans=  0
        for end in range(len(nums)):
            
            if (nums[end] == max_element):
                cnt += 1
            while cnt == k:
                if nums[start] == max_element:
                    cnt -= 1
                start += 1
            ans += start
        return ans