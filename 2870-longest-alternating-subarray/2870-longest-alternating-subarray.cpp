class Solution {
public:
    int alternatingSubarray(vector<int>& nums) {
        int ret = -1;
        int n = nums.size();
        for (int i = 0; i+1 < n; i++) {
            if (nums[i] + 1 != nums[i+1]) continue;
            int cur = 2;
            for (int j = 2; i+j < n; j++) {
                if (nums[i+j%2] == nums[j+i]) cur++;
                else break;
            }
            ret = max(ret, cur);
            
        }
        return ret;
        
    }
};