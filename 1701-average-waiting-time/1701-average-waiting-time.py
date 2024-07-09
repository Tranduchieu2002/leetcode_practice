class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_waiting_time = 0
        current_time = 0

        for arrival, service in customers:
            if current_time < arrival:
                current_time = arrival
            waiting_time = current_time - arrival + service
            total_waiting_time += waiting_time
            current_time += service

        return total_waiting_time / len(customers)