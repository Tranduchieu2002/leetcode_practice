from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        n = len(s)
        pq = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(pq)
        print(pq)
        if pq[0][0] > (n + 1) // 2:
            return ""
        ans = ["" for _ in range(n)]
        while len(pq) >= 2:
            (f1, c1) = heapq.heappop(pq)
            (f2, c2) = heapq.heappop(pq)
            
            if f1 + 1 < 0:
                heapq.heappush(pq, (f1 + 1, c1))
            if f2 + 1 < 0:
                heapq.heappush(pq, (f2 + 1, c2))
            ans.append(c1 + c2)
        if len(pq) == 1:
            (f1, c1) = heapq.heappop(pq)
            if f1 != -1:
                return ""
            else:
                ans.append(c1)
        return "".join(ans)
