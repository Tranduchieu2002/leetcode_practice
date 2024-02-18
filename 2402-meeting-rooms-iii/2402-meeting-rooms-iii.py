class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        ans = [0] * n
        pq = [] 

        availables = list(range(n))
        busy_rooms = []

        meetings.sort()

        for start, end in meetings:
            range_time = end - start
            # Free up rooms whose meetings have ended
            while busy_rooms and busy_rooms[0][0] <= start:
                freed_end, freed_index = heappop(busy_rooms)
                heappush(availables, freed_index)

            if availables:
                # Allocate room from available rooms
                available_room = heappop(availables)
                ans[available_room] += 1
                heappush(busy_rooms, (end, available_room))
            else:
                freed_end, index = heappop(busy_rooms)
                # when we + range time we will know when room in index finnished and holding will increase
                heappush(busy_rooms, (freed_end + range_time, index))
                ans[index] += 1

        # Find the most booked room
        res, m = 0, 0
        for i in range(n):
            if ans[i] > m:
                res = i
                m = ans[i]
        return res
