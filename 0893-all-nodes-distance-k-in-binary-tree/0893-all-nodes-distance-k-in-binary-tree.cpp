/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    unordered_map<TreeNode*,TreeNode*> mp;// map to store the parent nodes of all nodes
    void add_parent(TreeNode *curr,TreeNode *parent) {
        if(!curr) return ;// base case

        if(!parent) parent = curr;// root of the tree

        else mp[curr] = parent;//insert the key and value

        // traverse to left and rigth subtree to store all the parent nodes of nodes in the tree
        add_parent(curr->left,curr);

        add_parent(curr->right,curr); 
    }
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        // q - queue for breadth first search , visited map so that each node is visited once
        queue<TreeNode*> q;
        unordered_map<int,int> visited;
        vector<int> ans;

        add_parent(root,NULL);//calling add_parent to use the mp map

        q.push(target);// starting node will be our given target just like in graphs
        
        while(k-- && !q.empty()) { // will continue till it has reached a distance of k or level k 
            int size = q.size();

            while(size--) {
                TreeNode *Node = q.front();
                q.pop();
                visited[Node->val] = 1;// marking the node as visited

                // now visiting all the neighboring nodes to the target
                if(Node->left && visited[Node->left->val] != 1 ) 
                    q.push(Node->left);
                   
                if(Node->right && visited[Node->right->val] != 1 ) 
                    q.push(Node->right);

                if(mp[Node]  && visited[mp[Node]->val] != 1 ) 
                    q.push(mp[Node]);
                
            }
        }

        // creating the ans array 
        while(!q.empty()) {
            ans.push_back(q.front()->val);
            q.pop();          
        }

        return ans;
    }
};