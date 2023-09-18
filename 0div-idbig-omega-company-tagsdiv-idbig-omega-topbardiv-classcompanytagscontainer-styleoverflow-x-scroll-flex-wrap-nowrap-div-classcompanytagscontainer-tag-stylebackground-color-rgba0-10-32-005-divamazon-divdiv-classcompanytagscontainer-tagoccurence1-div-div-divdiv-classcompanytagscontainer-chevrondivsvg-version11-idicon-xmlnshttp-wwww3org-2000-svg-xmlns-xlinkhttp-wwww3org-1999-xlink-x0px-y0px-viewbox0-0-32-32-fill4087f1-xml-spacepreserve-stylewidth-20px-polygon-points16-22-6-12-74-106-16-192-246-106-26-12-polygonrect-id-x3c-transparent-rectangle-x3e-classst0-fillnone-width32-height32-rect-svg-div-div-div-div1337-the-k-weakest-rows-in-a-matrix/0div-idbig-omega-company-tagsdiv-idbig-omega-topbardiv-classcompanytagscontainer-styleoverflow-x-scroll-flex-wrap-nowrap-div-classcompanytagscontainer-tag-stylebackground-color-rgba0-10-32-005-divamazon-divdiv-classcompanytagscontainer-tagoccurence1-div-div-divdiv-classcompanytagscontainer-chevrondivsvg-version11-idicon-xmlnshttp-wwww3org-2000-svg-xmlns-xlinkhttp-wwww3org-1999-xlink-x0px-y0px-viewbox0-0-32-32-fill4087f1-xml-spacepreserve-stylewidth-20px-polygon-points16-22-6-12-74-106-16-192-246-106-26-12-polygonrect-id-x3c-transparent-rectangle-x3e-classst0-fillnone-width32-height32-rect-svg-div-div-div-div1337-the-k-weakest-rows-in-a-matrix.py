class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        min_heap = []
        def search(a):
            l, r = 0, len(a) - 1
            while l <= r:
                mid = (r - l) // 2 + l
                if a[mid] == 0:
                    r = mid - 1
                else:
                    l = mid + 1
            return l
        for i, row in enumerate(mat):
            soldiers_count = search(mat[i])
            
            heapq.heappush(min_heap, (soldiers_count, i))
        weakest_rows = [heapq.heappop(min_heap)[1] for _ in range(k)]

        return weakest_rows