class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        for(int i = 1; i < nums.size();++i) {
            int s1 = nums[i - 1];
            int s2 = nums[i];
            if(!(s1 ^ s2)) {
                return true;
            }
        }
        return false;
    }
};