class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        dict = set()
        counters = [0] * n
        for (c1, c2) in  roads:
            counters[c1] += 1
            counters[c2] += 1
            dict.add((c1, c2))
            dict.add((c2, c1))
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                ans = max(counters[i] + counters[j] - int((i, j) in dict), ans)
        return ans