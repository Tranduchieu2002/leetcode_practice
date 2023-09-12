class Solution:
    def minDeletions(self, s: str) -> int:
        counter = [0] * 26
        deletions = 0
        for c in s:
            counter[ord(c) - ord('a')] += 1
        freqs_set = set()
        for freq in counter:
            while freq > 0 and freq in freqs_set:
                freq -= 1
                deletions += 1
            freqs_set.add(freq)
        return deletions