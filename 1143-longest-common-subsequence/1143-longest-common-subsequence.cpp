class Solution {
    string s1, s2;
    vector<vector<int>> dp;
public:
    int solve(int i, int j) {
        if(i >= s1.size() || j >= s2.size()) return 0;
        int ans = 0;
        if(dp[i][j] != -1) return dp[i][j];
        if(s1[i] == s2[j]) {
            ans += solve(i + 1, j + 1) + 1;
        } else
            ans += max(solve(i + 1, j), solve(i, j + 1));
        return dp[i][j] = ans;
    }
    int longestCommonSubsequence(string text1, string text2) {
        s1 = text1;
        s2 = text2;
        dp.resize(s1.size(), vector<int>(s2.size(), -1));
        return solve(0,0);
    }
};