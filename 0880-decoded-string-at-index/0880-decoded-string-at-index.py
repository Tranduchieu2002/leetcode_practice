class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        ans = 0
        decode_len = 0
        n = len(s)
        for i in range(n):
            if s[i].isnumeric():
                decode_len *= int(s[i])
            else:
                decode_len += 1
        for i in range(n - 1, - 1, -1):
            if s[i].isnumeric():
                decode_len //= int(s[i])
                k = k % decode_len
            else:
                if decode_len == k or k == 0:
                    return s[i]
                decode_len -= 1
        return ""