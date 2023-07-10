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
    int minDepth(TreeNode* root) {
        return dfs(root);
    }
    int dfs(TreeNode *root) {
        if(!root) {
            return 0;
        }
        if(!root->right and !root->left) {
            return 1;
        }
        int ans = INT_MAX;
        if(root->right) {
            ans = min(ans, dfs(root->right));
        }
        if(root->left) {
            ans = min(ans, dfs(root->left));
            cout << ans << "  ";
        }

        return ans + 1;
    }
};