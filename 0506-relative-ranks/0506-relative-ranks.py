class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        memo = defaultdict(int)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        max_score = max(score)
        
        tempIdx = [None] * (max_score + 1)
        for i in range(len(score)):
            tempIdx[score[i]] = i
        ranks = [""] * len(score)
        temp = 0
        for i in range(max_score, -1, -1):
            if tempIdx[i] is None:
                continue
            if temp <= 2:
                ranks[tempIdx[i]] = medals[temp]
            else:
                ranks[tempIdx[i]] = str(temp + 1)
            temp += 1
                
        return ranks