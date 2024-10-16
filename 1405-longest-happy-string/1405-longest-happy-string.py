class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))

        result = []
        
        while heap:
            lc1, c1 = heapq.heappop(heap)
            if len(result) >= 2 and result[-1] == result[-2] == c1:
                if not heap:
                    break
                lc2, c2 = heapq.heappop(heap)
                if (lc2 + 1 != 0):
                    heapq.heappush(heap, (lc2 + 1, c2))
                result.append(c2)
            result.append(c1)
        
            if (lc1 + 1 != 0):
                heapq.heappush(heap, (lc1 + 1, c1))
        return ''.join(result)