//
// Created by michael on 22/06/2023.
//          Question 63 leetcode
//Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
//Output: 2
//Explanation: There is one obstacle in the middle of the 3x3 grid above.
//There are two ways to reach the bottom-right corner:
//1. Right -> Right -> Down -> Down
//2. Down -> Down -> Right -> Right
//

#include <bits/stdc++.h>
using namespace std;
class Solution {
    int n, m;
    int dp[100][100];
    vector<vector<int>> g;
    int ways = 0;
public:
    int findPath(int i, int j) {
        if(i == n || j == m || g[i][j] == 1) return 0; // skip when end line and met obstacle

        if(i == n - 1 && j == m - 1) return 1; // came down - right coner

        if (dp[i][j])
            return dp[i][j];

        int down = 0;
        int right = 0;

        down = findPath(i + 1, j);
        right = findPath(i, j + 1);

        return dp[i][j] = down + right;
    }
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        g = obstacleGrid;
        n = g.size();
        m = g[0].size();
        return findPath(0,0);
    }
};
