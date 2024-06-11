class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        temp = [0] * 1001
        ans = []
        for val in arr1:
            temp[val] += 1
        for val in arr2:
            ans.extend([val] * temp[val])
            temp[val]= 0
        for val in range(1001):
            if temp[val] == 0:
                continue
            ans.extend([val] * temp[val])
        return ans