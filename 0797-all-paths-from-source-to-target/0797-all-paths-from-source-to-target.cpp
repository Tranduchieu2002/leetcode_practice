class Solution {
private: 
    vector<vector<int>> ans;
    int  n;
public:
    void backtrack(int i, vector<int> &res, vector<vector<int>> adj) {
        res.push_back(i);
        if(i == n - 1) {
            ans.push_back(res);
            return;
        }
        for(int it : adj[i]) {
            backtrack(it, res, adj);
            res.pop_back();
        }
    }
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        n = graph.size();
        vector<vector<int>> adj = graph;

        vector<int> res;
        backtrack(0, res, adj);
        
        return ans;
        
    }
};