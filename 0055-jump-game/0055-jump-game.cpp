class Solution {
    vector<int> memo;
public:
    bool solve(int i, vector<int>& nums) {
        if (i == nums.size() - 1) return true;
        if (nums[i] == 0) return false;
        if (memo[i] != -1) return memo[i];
        for (int idx = 1; idx <= nums[i]; ++idx) {
            if (i + idx < nums.size() && solve(i + idx, nums)) return memo[i] = true;
        }
        return memo[i] = false;
    }
    
    bool canJump(vector<int>& nums) {
        memo.resize(nums.size(), -1);
        return solve(0, nums);
    }
};
