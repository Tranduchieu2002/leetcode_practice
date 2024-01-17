class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = defaultdict(int)
        occurs = set()
        for i in arr:
            freq[i] += 1
        
        for val in freq.values():
            if val in occurs:
                return False
            
            occurs.add(val)
            
        return True