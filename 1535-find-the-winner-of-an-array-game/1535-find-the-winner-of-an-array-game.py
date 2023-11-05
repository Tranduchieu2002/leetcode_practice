class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n:
            return max(arr)
        count = 0
        winner = arr[0]
        dq = deque(arr[1:])
        
        while count < k:
            if winner > dq[0]:
                count += 1
            else:
                count = 1
                winner = dq[0]
            dq.popleft()
            dq.append(winner)

        return winner
