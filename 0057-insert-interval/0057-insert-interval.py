class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        
        intervals.sort(key=lambda z:z[0])
        ans = []
        for i in intervals:
            if ans and ans[-1][1] >= i[0]:
                ans[-1][1] = max(i[1], ans[-1][1])
            else:
                ans.append(i)
        return ans