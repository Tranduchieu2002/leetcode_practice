class Solution {
public:
    int n;
    vector<int> nums;
    bool PredictTheWinner(vector<int>& nums) {
        if(nums.size() == 1) return true;
        n = nums.size();
        this->nums = nums;
        vector<vector<int>> dp(n - 1, vector<int>(n, -1));
        int sum = 0;

        for(auto val : nums) {
            sum += val;
        }
        
        solve(0, n - 1, dp);

        for(auto v1 : dp) {
            for(auto v2: v1) {
                cout << v2 << "  ";
            }
            cout << endl;
        }
        return dp[0][n - 1] >= 0;
        
    }
    int solve(int i, int j, vector<vector<int>> &dp) {
        if(i > j) return 0;

        if(i == j) return nums[i];
        
        if(dp[i][j] != -1) return dp[i][j];
        
        int takeHead = nums[i] - solve(i + 1, j, dp);

        int takeTail = nums[j] - solve(i, j - 1, dp);
            
        return dp[i][j] = max(takeHead, takeTail);            
    }
};