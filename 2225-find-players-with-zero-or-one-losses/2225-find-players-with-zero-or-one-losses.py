class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        looserDict = defaultdict(int)
        players = set()

        for winner, looser in matches:
            players.add(winner)
            players.add(looser)
            looserDict[looser] += 1

        ans = [[], []]

        for player in players:
            if player not in looserDict:
                ans[0].append(player)

            if looserDict[player] == 1:
                ans[1].append(player)

        ans[0].sort()
        ans[1].sort()

        return ans