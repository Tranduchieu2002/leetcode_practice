class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        deletions = 0
        freqs_set = set()
        for char, freq in counter.items():
            while freq > 0 and freq in freqs_set:
                freq -= 1
                deletions += 1
            freqs_set.add(freq)
        return deletions