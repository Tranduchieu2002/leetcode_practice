class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        ans_left, ans_right = 0, 0
        left, right = 0, n -1
        nowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while left <= right:
            if s[left] in nowels:
                ans_left += 1
            if s[right] in nowels:
                ans_right += 1
            left += 1
            right -= 1
        return ans_left == ans_right