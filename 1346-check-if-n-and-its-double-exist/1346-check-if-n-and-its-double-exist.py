class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Sort the array to use binary search
        arr.sort()
        
        for i, num in enumerate(arr):
            # Find the index where `2 * num` could be
            index = bisect.bisect_left(arr, num * 2)
            
            # Ensure the index is within bounds and not the same as `i`
            if index != len(arr) and index != i and arr[index] == num * 2:
                return True
        
        return False