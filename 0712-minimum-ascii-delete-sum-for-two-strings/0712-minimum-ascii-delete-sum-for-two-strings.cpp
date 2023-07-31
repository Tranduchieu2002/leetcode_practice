class Solution {
    string s1, s2;
    int n, m;
    vector<vector<int>> dp;
public:
    int solve(int i, int j) {
        if(i >= n && j >= m) return 0;
        if(dp[i][j] != -1) return dp[i][j];
        if(i >= n) {
            int sum = 0;
            for(int idx = j; idx < m; ++idx) {
                sum += s2[idx];
            }
            dp[i][j] = sum;
            return sum;
        }
        if(j >= m) {
            int sum = 0;
            for(int idx = i; idx < n; ++idx) 
                sum += s1[idx];
            dp[i][j] = sum;
            return sum;
        }
        int ans = INT_MAX;
        if(s1[i] == s2[j]) {
            ans = solve(i + 1, j + 1);
        } else {
            ans = min(ans, s1[i] + solve(i + 1, j));
            ans = min(ans, s2[j] + solve(i, j + 1));
        }
        dp[i][j] = ans;
        return ans;
    }
    int minimumDeleteSum(string s1, string s2) {
        this->s1 = s1;
        this->s2 = s2;
        n = s1.size();
        m = s2.size();
        dp.resize(n + 1, vector<int>(m + 1, -1));
        return solve(0,0);
    }
};