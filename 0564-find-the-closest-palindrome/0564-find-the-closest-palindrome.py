class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        candidates = set()

        if n == "1":
            return "0"

        prefix = n[:(length + 1) // 2]
        prefix_number = int(prefix)

        for i in [-1, 0, 1]:
            new_prefix = str(prefix_number + i)
            if length % 2 == 0:
                candidate = new_prefix + new_prefix[::-1]
            else:
                candidate = new_prefix + new_prefix[:-1][::-1]
            candidates.add(candidate)

        candidates.add(str(10**(length - 1) - 1))
        candidates.add(str(10**length + 1))

        candidates.discard(n)

        closest_palindrome = None
        min_difference = float('inf')
        num = int(n)
        
        for candidate in candidates:
            candidate_num = int(candidate)
            difference = abs(candidate_num - num)
            if difference < min_difference or (difference == min_difference and candidate_num < int(closest_palindrome)):
                min_difference = difference
                closest_palindrome = candidate

        return closest_palindrome
