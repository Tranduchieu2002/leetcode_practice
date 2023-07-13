class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        if(n <= 1) {
            return nums[0];
        }
        int maxEndHere = 0, maxSoFar = INT_MIN;

        for(int i = 0; i < n;++i) {
            maxEndHere += nums[i];

            maxSoFar = max(maxSoFar, maxEndHere); 
            if(maxEndHere < 0) { // dont get here
                maxEndHere = 0;
            }
        }
        return maxSoFar;
    }
};