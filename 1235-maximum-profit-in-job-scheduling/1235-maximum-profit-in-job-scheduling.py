class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        schedules = []
        n = len(startTime)
        for i in range(n):
            start, end, pro = startTime[i], endTime[i], profit[i]
            schedules.append((start, end, pro))
        
        schedules.sort(key=lambda x:x[0])
        print(schedules)
        pq = []
        maxProfit = 0
        for i in range(n):
            while pq and pq[0][0] <= schedules[i][0]:
                
                maxProfit = max(heapq.heappop(pq)[1], maxProfit )
            
            heapq.heappush(pq, (schedules[i][1], maxProfit + schedules[i][2]))
        for (end, val) in pq:
            maxProfit = max(maxProfit, val)
        
        return maxProfit