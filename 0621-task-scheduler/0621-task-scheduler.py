class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        max_sl = 0
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
            max_sl = max(max_sl, freq[ord(task) - ord('A')])
            
        max_time = (max_sl - 1) * (n + 1)
        for f in freq:
            if f == max_sl:
                max_time +=1
        return max(len(tasks), max_time)
            
    