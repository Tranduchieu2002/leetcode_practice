class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = defaultdict(int)
        
        for bit in s:
            cnt[bit] += 1
        
        if cnt['1'] == 2:
            return '1' + '0' * cnt['0'] + '1'
        
        if cnt['1'] == 1:
            return '0' * cnt['0'] + '1'
        
        return '1' * (cnt['1'] - 1) + '0' * cnt['0'] + '1'