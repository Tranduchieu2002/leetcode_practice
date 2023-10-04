class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        def cmp(trip1, trip2):
            if trip1[1] == trip2[1]:
                return trip1[2] - trip2[2]
            return trip1[1] - trip2[1] 
        key = cmp_to_key(cmp)
        trips = sorted(trips, key=key) 
        # print(trips)
        pq = []
        heapq.heapify(pq)
        cur_cap = 0
        for i in range(len(trips)):
            # if pq:
            #     print(pq, pq[-1][0], trips[i][1])
            while pq and pq[0][0] <= trips[i][1]:
                smaller_cur = heapq.heappop(pq)
                print('yesy')
                cur_cap -= smaller_cur[1]
            cur_cap += trips[i][0]
            heapq.heappush(pq, (trips[i][2], trips[i][0]))
            if cur_cap > capacity:
                return False
            
        return True
            