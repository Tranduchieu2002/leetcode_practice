class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int n = nums.size();
        if (n == 1 and nums[0] == target) {
            return {0, 0};
        }
        
        int left = 0, right = n - 1;
        while (left <= right) {
            int mid = (right  - left) / 2 + left;
            
            if (nums[mid] == target) {
                int first, last;
                first = last = mid;
                while (first > 0 and nums[first - 1] == target) {
                    first --;
                }
                while (last < n - 1 and nums[last + 1] == target) {
                    last ++;
                }
                return {first, last};
//                 if (mid < n - 1 and nums[mid + 1] == target) {
//                     return { mid, mid + 1 };
//                 }
//                 if (mid > 0 and nums[mid - 1] == target) {
//                     return { mid - 1, mid };
//                 }
                
//                 return {mid , mid};
            }
            
            if (nums[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        
        return {-1, -1};
    }
};