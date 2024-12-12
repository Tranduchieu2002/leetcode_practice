class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-i for i in gifts]
        heapq.heapify(gifts)
        ans = 0
        while k > 0:
            largest = heapq.heappop(gifts)
            heapq.heappush(gifts, -math.isqrt(-largest))
            k -= 1 
        return -sum(gifts)