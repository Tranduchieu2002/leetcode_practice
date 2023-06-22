#include <bits/stdc++.h>
using namespace std;
class Solution {
    int m, n;
    int dp[100][100];
public:
    int uniquePaths(int m, int n) {
        this->m = m;
        this->n = n;
        memset(dp, -1, sizeof(dp));
        return findPath(0,0);
    }

    int findPath(int i, int j) {
        if(i == m || j == n) return 0;

        if(i == m - 1 && j == n - 1) return 1;

        if (dp[i][j] != -1)
            return dp[i][j];

        int down = 0;
        int right = 0;

        down = findPath(i + 1, j);
        right = findPath(i, j + 1);

        return dp[i][j] = down + right;
    }
};

// example with m = 3, n = 7 ans = 28