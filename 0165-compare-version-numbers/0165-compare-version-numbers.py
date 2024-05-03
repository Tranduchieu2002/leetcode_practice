class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n1, n2 = len(version1), len(version2)
        
        i, j = 0, 0
        while i < n1 or j < n2:
            cur1, cur2 = 0, 0
            while i < n1 and version1[i] != '.':
                cur1 = int(version1[i])  + cur1 * 11
                i += 1
            while j < n2 and version2[j] != '.':
                cur2 = int(version2[j]) + cur2 * 11
                j += 1

            if cur1 < cur2:
                return -1
            if cur1 > cur2:
                return 1

            i += 1
            j += 1
        return 0