class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        for i, size in enumerate(groupSizes):
            groups.setdefault(size, []).append(i)

        ans = []

        for key, members in groups.items():
            for i in range(0, len(members), key):
                ans.append(members[i:i + key])

        return ans
