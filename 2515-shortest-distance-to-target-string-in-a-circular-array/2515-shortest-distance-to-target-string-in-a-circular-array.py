class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans, n = 101, len(words)
        
        for i in range(n):
            if words[i] == target:
                
                ans = min(ans,abs(startIndex - i),abs(n - abs(startIndex - i)))
#         not found
        if ans == 101:
            return -1
        return ans