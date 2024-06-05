class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(ord('a'), ord('z') + 1):
            c = chr(i)
            minCnt = float('inf')
            for w in words:
                cnt = w.count(c)
                
                if cnt == 0:
                    break;
                
                minCnt = min(cnt, minCnt)
            if cnt >= 1 and cnt != float('inf'):
                ans.extend(c * minCnt)
        
        return ans
            