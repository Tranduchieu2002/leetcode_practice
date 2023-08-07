class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans = 0
        
        n =  len(nums)
        len_distinc = len(set(nums))
        mp = {}
        # burce force (TLE)
        # for i in range(n):
        #     for j in range(i + 1, n + 1):
        #         subarray = nums[i:j]
        #         if(len(distinc) == len(set(subarray))): 
        #             ans += 1
        
        right, left = 0 ,0
        while(right < n):
            val = nums[right]
            mp[val] =mp[val] + 1 if val in mp else 1
            if(mp[val] == 1): 
                len_distinc -= 1
            while(len_distinc == 0):
                mp[nums[left]] -= 1
                if(mp[nums[left]] == 0):
                    len_distinc += 1
                left +=1
            ans += left
            right+=1
        
        return ans
            