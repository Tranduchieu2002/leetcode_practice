class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        groups = [i for i in range(n)]
        groups[firstPerson] = 0

        meetings.sort(key=lambda x: x[2])

        size = len(meetings)
        i = 0
        while i < size:
            current_time = meetings[i][2]
            temp = []
            while i < size and meetings[i][2] == current_time:
                g1 = self.find(groups, meetings[i][0])
                g2 = self.find(groups, meetings[i][1])
                groups[max(g1, g2)] = min(g1, g2)
                temp.extend([meetings[i][0], meetings[i][1]])
                i += 1
            for j in temp:
                if self.find(groups, j) != 0:
                    groups[j] = j

        result = []
        for j in range(n):
            if self.find(groups, j) == 0:
                result.append(j)

        return result

    def find(self, groups: List[int], index: int) -> int:
        while index != groups[index]:
            index = groups[index]
        return index
