class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        memo = {}

        def dp(i, m, player_turn):
            if i >= n:
                return 0
            if (i, m, player_turn) in memo:
                return memo[(i, m, player_turn)]

            if player_turn == 0:  # Alice's turn, maximize score
                max_score = float('-inf')
                stone_sum = 0
                for j in range(1, min(2 * m, n - i) + 1):
                    stone_sum += piles[i + j - 1]
                    max_score = max(max_score, stone_sum + dp(i + j, max(m, j), 1))
                memo[(i, m, player_turn)] = max_score
                return max_score
            else:  # Bob's turn, minimize Alice's score
                min_score = float('inf')
                for j in range(1, min(2 * m, n - i) + 1):
                    min_score = min(min_score, dp(i + j, max(m, j), 0))
                memo[(i, m, player_turn)] = min_score
                return min_score

        total_sum = sum(piles)
        alice_score = dp(0, 1, 0)
        return alice_score
