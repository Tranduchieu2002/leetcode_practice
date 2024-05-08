class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        i, j = 0, 0
        memo = defaultdict(int)
        n = len(word)
        predict_max = 0
        temp = ""
        for i in range(k):
            temp += word[i]
        memo[temp] += 1
        while i < n:
            temp, j = "", i + 1
            while j < i + k + 1 and j < n:
                temp += word[j]
                j += 1
    
                
            memo[temp] += 1
            predict_max = max(memo[temp], predict_max)
            i += k
        return n // k - predict_max
                