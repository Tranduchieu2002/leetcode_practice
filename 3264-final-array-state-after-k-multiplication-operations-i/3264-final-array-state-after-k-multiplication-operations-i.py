class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(val, i) for i, val in enumerate(nums)]
        heapq.heapify(heap)
        
        while k > 0:
            minItem = heapq.heappop(heap)
            minVal, i = minItem 
            
            newVal = minVal * multiplier
            
            heapq.heappush(heap, (newVal, i))
            
            nums[i] = newVal
            
            k -= 1
        return nums
    