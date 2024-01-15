class Solution:
    def karbinKarp(self, s, v):
        n, k = len(s), len(v)
        
        if k > n:
            return []
        mod = 10 ** 9 + 7
        h_w = 0
        h = [0] * (n + 1)
        p = [1] * (n + 1)
        base = 10
        def getHash(i, j):
            return (h[j] - h[i - 1] * p[j - i + 1] + mod) % mod  # Fixed: Add mod and fix the subtraction
        for i in range(1, n + 1):
            h[i] = ((h[i - 1] * base) + ord(s[i - 1])) % mod
            p[i] = (p[i - 1] * base) % mod
        
        for i in range(1, k + 1):
            h_w = (h_w * base + ord(v[i - 1])) % mod
        l = []
        for i in range(1, n - k + 2):
            isQual = getHash(i, i - 1 + k) == h_w
            if isQual:
                l.append(i - 1)
        return l
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        idx_1, idx_2 = self.karbinKarp(s, a), self.karbinKarp(s, b)
        beautiful_indices = []

#         def find_b_occurrences(s, b, start_index, end_index) -> List[int]:
#             b_occurrences = []
#             for i in range(start_index, end_index - len(b) + 1):  # Use len(b) for consistency
#                 if s[i:i + len(b)] == b:
#                     b_occurrences.append(i)
#             return b_occurrences

#         last_b_index = -1  # Track the last seen b index

#         for i in range(len(s) - len(a) + 1):  # Use len(a) for consistency
#             if s[i:i + len(a)] == a:
#                 # Check for a valid b occurrence within the k-window
#                 if last_b_index != -1 and i - last_b_index <= k:
#                     beautiful_indices.append(i)
#                 elif last_b_index == -1:
#                     # If no b occurrence found yet, pre-calculate b occurrences for the first k-window
#                     b_occurrences = find_b_occurrences(s, b, i, i + k)
#                     if b_occurrences:
#                         last_b_index = b_occurrences[0]  # Update last_b_index
#                         beautiful_indices.append(i)
        ans = []
        for i in range(len(idx_1)):
            val = idx_1[i]
            bl, br = bisect_left(idx_2, val - k), bisect_right(idx_2, val + k)
            # meaning we cannot find any solution in [val - k, val = k]
            # print(bn, br)
            # 16, 31
            
            if br - bl:
                ans.append(val)                

        return ans
