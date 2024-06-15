class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        n = len(profits)
        ps = [(capital[i], profits[i]) for i in range(n)]
        
        ps.sort()
        max_heap = []
        tempIdx = 0
        for i in range(k):
            while tempIdx < n and ps[tempIdx][0] <= w:
                heapq.heappush(max_heap, -ps[tempIdx][1])
                tempIdx += 1
            
            if max_heap:
                w -=heapq.heappop(max_heap)
            
        return w