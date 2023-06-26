//
// Created by michael on 26/06/2023.
//

#ifndef ALGO_SOLUTION_H
#define ALGO_SOLUTION_H
#include <bits/stdc++.h>

using namespace std;

class Solution {
    int n;
    int m;
    int dx[4] = {0, 0, -1, 1};
    int dy[4] = {-1, 1, 0, 0};
    vector<vector<int>> memo;
    bool validDis(int i , int j) {
        return !(i < 0 || i >= n || j < 0 || j >= m);
    }
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        n =  matrix.size();
        m =  matrix[0].size();
        int ans = INT_MIN;
        memo.resize(n + 1, vector<int>(m + 1, -1));
        for(int i =0; i < n; ++i)
            for(int j = 0; j < m; ++j)
                ans = max(ans, dfs(i,j, matrix));

        return ans + 1;
    }
    int dfs(int i, int j, vector<vector<int>>& matrix) {
        int ans = 0;
        if(memo[i][j] != -1) return memo[i][j];
        for(int d = 0; d < 4; ++d) {
            int x = dx[d] + i, y = dy[d] + j;
            string s =  validDis(x, y) ? "true" : "false";
            if(validDis(x, y) &&  matrix[x][y] > matrix[i][j]) {
                ans = max(ans, dfs(x,y, matrix) + 1);
            }
        }
        return memo[i][j] = ans;
    }
};


#endif //ALGO_SOLUTION_H
