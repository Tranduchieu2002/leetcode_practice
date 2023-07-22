class Solution {
    vector<int> memo;
public:
    bool solve(int i,int n, vector<int>& nums) {
        if (i == n - 1) return true;
        if (nums[i] == 0) return false;
        if (memo[i] != -1) return memo[i];
        for (int idx = 1; idx <= nums[i]; ++idx) {
            if (i + idx < n && solve(i + idx, n, nums)) return memo[i] = true;
        }
        return memo[i] = false;
    }
    
    bool canJump(vector<int>& nums) {
        memo.resize(nums.size(), -1);
        return solve(0, nums.size(), nums);
    }
};
