class Solution {
public:
    vector<int> getRow(int rowIndex) {
        if (rowIndex == 0) return {1};
        if (rowIndex == 1) return {1, 1};
        vector<int> ans = {1, 1};
        int index = 2; 
        while (index <= rowIndex) {
            vector<int> temp = {1};
            while (temp.size() < (index)) {
                temp.push_back(ans[temp.size() - 1] + ans[temp.size()]);
            }
            temp.push_back(1);
            ans = temp;
            index ++;
            
        }
        return ans;
    }
};