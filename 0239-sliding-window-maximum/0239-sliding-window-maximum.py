class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 1 or k == 1:
            return nums
        ans = [0] * (n - k + 1)
        left , right = 0, 0
        dq = deque()
        
        while right < n:
            while dq and dq[-1] < right - k + 1:
                dq.pop()
            
            while dq and nums[dq[0]] < nums[right]:
                dq.popleft()
            
            dq.appendleft(right)
            if right >= k - 1:
                ans[left] = nums[dq[-1]]
                left += 1
            right += 1
        return ans
            