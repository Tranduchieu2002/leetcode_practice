class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        def isOdd(i):
            result = True
            for i in range(i, i + 3):
                if arr[i] % 2 == 0:
                    return False
            return True
        for i in range(0, n - 2):
            if isOdd(i):
                return True
        return False