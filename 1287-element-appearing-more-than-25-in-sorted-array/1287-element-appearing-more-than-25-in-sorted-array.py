class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        # when ques appear we must try to think ques can solve by binary search
        # In this ques as we see It's have more than 1 / 4  elements => we will check element in 3 points is
        # 1 / 4 , 2 / 4, 3 / 4
        n = len(arr)
        ans , points = -1, [n // 4, n // 2, 3 * n // 4]
        
        for point in points:
            left  = bisect_left(arr, arr[point])
            right  = bisect_right(arr, arr[point]) 
            
            if right - left  > n // 4:
                return arr[left]
            
        return -1
                