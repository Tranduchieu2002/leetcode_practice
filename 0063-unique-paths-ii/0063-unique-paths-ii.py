class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        n, m = len(g), len(g[0])
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                if i==0 and j==0 and g[i][j] == 0:
                    print('t')
                    dp[i][j]=1;
                    continue;
                
                if(g[i][j]):
                    dp[i][j]=0;
                    continue;
                
                st1, st2 = 0, 0;
                
                if(i>0):
                    st1=dp[i-1][j]
                    
                if(j>0):
                    st2 = dp[i][j-1]
                    
                dp[i][j]=st1+st2;
                
        return dp[n - 1][m - 1]