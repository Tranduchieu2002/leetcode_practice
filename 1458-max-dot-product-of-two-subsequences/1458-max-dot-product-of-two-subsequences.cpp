class Solution {
    vector<vector<int>> memo;
    int n, m;
    vector<int> nums1, nums2;
public:
    int dp(int i, int j) {
        if (i == n or j == m) return INT_MIN;
        
        if (memo[i][j] != -1) return memo[i][j];
        
        int ans = max({
           (nums1[i] * nums2[j]) + max(dp(i + 1, j + 1), 0) ,
            dp(i , j + 1),
            dp(i + 1, j)
        });
        
        memo[i][j] = ans;
        
        return ans;
    }
    int maxDotProduct(vector<int>& nums1, vector<int>& nums2) {
        this->n = nums1.size(), this->m = nums2.size();
        this->nums1 = nums1;
        this->nums2 = nums2;
        this->memo = vector<vector<int>>(this->n, vector<int>(this->m, -1));
        
        int res = dp(0, 0);
        // if (res == 0) {
        //     return max(nums1[0] * nums2[m - 1],
        //               nums1[n - 1] * nums2[0]);
        // }
        return res;
    }
};