class SeatManager:

    def __init__(self, n: int):
        self.seats = [i for i in range(1, n + 1)]
        heapq.heapify(self.seats)

    def reserve(self) -> int:
        if self.seats is None:
            return -1
                    
        return heapq.heappop(self.seats)
            

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)