class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        
        starts, ends = [], []
        n = len(flowers)
        for start, end in flowers:
            starts.append(start)
            ends.append(end)
        
        starts.sort()
        ends.sort()
        ans = []
        for p in people:
            start = bisect_right(starts, p)
            end = bisect_left(ends, p)
            ans.append(start- end)
        return ans