class Solution {
public:
    bool canPlaceFlowers(vector<int>& nums, int n) {
        
        if(n == 0) return true;
        
        int i = 0;
        
        
        while(i < nums.size() && nums[i] == 1) {
            i++;
        }
        
        if(nums.size() == 1) return nums[0] == 0 && n == 1; 
        
//         if(i == nums.size() - 1 && )
        
        if (i == 0) {
            if (nums[i + 1] == 0 && nums[i] == 0) {
                n--;
                nums[i] = 1;
            }
            i++;
        }

        for (; i < nums.size() && n > 0; ++i) {
            if(nums.size() - 1 == i) {
                 if (nums[i - 1] == 0 && nums[i] == 0) {
                     n--;
                 }
                break;
            }
            if (nums[i - 1] == 0 && nums[i] == 0 && nums[i + 1] == 0) {
                nums[i] = 1;
                n--;
            }
        }

        return n == 0;
        
    }
};