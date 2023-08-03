class Solution {
    vector<vector<int>> ans;
public:
    void backtracking(vector<int>& candidates, int target, vector<int> &temps ,int i = 0) {
        
        if(target == 0){
            ans.push_back(temps);
            return;
        }
        while(i < candidates.size() && target - candidates[i] >= 0) {

            temps.push_back(candidates[i]);
            
            backtracking(candidates, target - candidates[i], temps, i);
            
            i++;

            temps.pop_back();
        }

    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> temp;
        sort(candidates.begin(), candidates.end());

//         auto last = std::unique(candidates.begin(), candidates.end());
//         candidates.erase(last, candidates.end());
        backtracking(candidates, target, temp, 0);
        return ans;
    }
};