class Solution:
    def firstUniqChar(self, s: str) -> int:
        # char_set = [0] * 26
        # dq = deque()
        # for i, c in enumerate(s):
        #     num_char = ord(c) - ord('a')
        #     char_set[num_char] += 1
        #     dq.append(i)
        #     while dq:
        #         if char_set[ord(s[dq[0]]) - ord('a')] > 1:
        #             dq.popleft()
        #         else:
        #             break
        # return  dq[0] if dq else -1
        
        chars = 'abcdefghijklmnopqrstuvwxyz'
        min_ans = float('inf')
        for c in (chars):
            first_find_i = s.find(c)
            if first_find_i == -1:
                continue
            right_find_i = s.rfind(c)
            if first_find_i == right_find_i:
                min_ans = min(min_ans, first_find_i)
        return -1 if min_ans == float('inf') else min_ans
            