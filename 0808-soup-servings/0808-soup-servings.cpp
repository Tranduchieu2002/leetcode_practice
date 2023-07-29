class Solution {
    int base[4][2] = {{100, 0}, {75, 25}, {50,50}, {25, 75}};
public:
    double solve(int A, int B, vector<vector<double>> &dp) {
        if(A <= 0 and B <= 0) {
            return 0.5;
        }
        
        if(A <= 0) return 1;
        
        if(B <= 0) return 0;
        
        if(dp[A][B] != -1.0) return dp[A][B];
        
        double ans = 0;
        for(auto val : base) {
            ans += solve(A - val[0], B - val[1], dp);
        }
        
        dp[A][B] = ans / 4;
        
        return dp[A][B];
    }
    
    double soupServings(int n) {
        if(n > 4800) return 1.0;
        vector<vector<double>> dp(n+ 1, vector<double>(n + 1, -1));
        return solve(n , n, dp);
    };
};