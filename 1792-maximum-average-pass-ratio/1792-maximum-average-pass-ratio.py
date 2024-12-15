class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        ratioClasses = []
        
        def profit(a, b):
            return (a + 1) / (b + 1) - a / b
        
        for item in classes:
            pass_student, total = item
            heapq.heappush(ratioClasses, (-profit(pass_student, total), pass_student, total))
        for _ in range(extraStudents):
            most_needed_smallest_profit = heapq.heappop(ratioClasses)
            plused_passed_student, plused_total_student = most_needed_smallest_profit[1] + 1, most_needed_smallest_profit[2] + 1
            heapq.heappush(ratioClasses, (-profit(plused_passed_student, plused_total_student), plused_passed_student, plused_total_student))
        
        ans  = sum(float(item[1]) / float(item[2])  for item in ratioClasses) / len(classes)
        return ans