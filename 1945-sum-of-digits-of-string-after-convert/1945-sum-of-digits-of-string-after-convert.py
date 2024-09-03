class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # convert
        ans = ""
        for c in s:
            num = ord(c) - ord('a') + 1
            ans += str(num)
        # transform
        while k > 0:
            num = 0
            for c in ans:
                num += int(c)
            ans = str(num)
            k -= 1
        return int(ans)