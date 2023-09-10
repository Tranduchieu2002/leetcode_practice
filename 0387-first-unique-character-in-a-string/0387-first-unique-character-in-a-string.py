class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_set = [0] * 26
        dq = deque()
        for i, c in enumerate(s):
            num_char = ord(c) - ord('a')
            char_set[num_char] += 1
            dq.append(i)
            while dq:
                if char_set[ord(s[dq[0]]) - ord('a')] > 1:
                    dq.popleft()
                else:
                    break
        return  dq[0] if dq else -1
            
            