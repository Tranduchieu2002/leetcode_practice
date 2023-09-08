class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = [[1]]
        
        for i in range(1, numRows):
            temp = [1]
            prev = ans[-1]
            for j in range(1, i):
                sum_item = prev[j - 1] + prev[j]  
                temp.append(sum_item)
            temp.append(1)
            ans.append(temp)
        
        return ans