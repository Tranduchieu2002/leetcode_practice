/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:

    vector<TreeNode*> allPossibleFBT(int n) {
        if(n % 2 == 0) return {};
        if(n == 1) return {new TreeNode()};
        vector<TreeNode*> ans;
        for(int i = 1; i < n; i += 2) {
            vector<TreeNode*> l = allPossibleFBT(i);
            vector<TreeNode*> r = allPossibleFBT(n - i - 1);
            
            for(auto nodeL : l)
                for(auto nodeR : r) {
                    ans.push_back(new TreeNode(0, nodeL, nodeR));
                }
        }
        return ans;
    }
};