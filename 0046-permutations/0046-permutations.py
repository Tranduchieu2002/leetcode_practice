class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        # Python3 program to swap elements
        # at given positions

        # Swap function
        def swap(lis, pos1, pos2):
            temp=lis[pos1]
            lis[pos1]=lis[pos2]
            lis[pos2]=temp
            return lis

        def solve(i:int, res: List[int]):
            if i == n:
                ans.append(res[:])
                return
            
            for j in range(i, n):
                swap(res,j,i) 
                solve(i + 1, res)
                swap(res, j , i)
            
        solve(0, nums)
        return ans