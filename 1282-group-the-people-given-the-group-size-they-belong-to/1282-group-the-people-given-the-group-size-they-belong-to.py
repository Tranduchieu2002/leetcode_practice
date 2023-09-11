class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        mp = {}
        n = len(groupSizes)

        for i in range(n):
            size = groupSizes[i]
            if size not in mp:
                mp[size] = []
            mp[size].append(i)

        ans = []

        for key in mp:
            totalNumberOfGroup = len(mp[key])
            perNumInGroup = totalNumberOfGroup // key
            temp = []

            for i in range(0, totalNumberOfGroup, key):
                temp.append(mp[key][i:i+key])

            ans.extend(temp)

        return ans