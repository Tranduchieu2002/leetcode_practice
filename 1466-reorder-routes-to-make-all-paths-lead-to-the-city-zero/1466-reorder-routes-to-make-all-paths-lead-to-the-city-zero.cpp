class Solution {
    int ans = 0;
public:
    // TLE
    void dfs(int i, vector<vector<int>> adj, vector<bool> flags) {
        flags[i] = true;
        for(auto  val : adj[i]) {
            if(!flags[abs(val)]) {
                if(val > 0) {
                    ans++;
                }
                dfs(abs(val), adj, flags);
            }
        }
    }
    int minReorder(int n, vector<vector<int>>& c) {
        vector<vector<int>> adj(n);
        for(int i = 0; i < c.size(); ++i) {
            int first = c[i][0];
            int second = c[i][1];
            // cout << first << "   " << second << endl;
            adj[first].push_back(second);
            adj[second].push_back(first * -1);
            // > 0 mean true route and then we just need to count who is true route
        }
        vector<bool> flags(n , false);
        flags[0] = true;
        queue<int> q;
        q.push(0);

        while(!q.empty()) {
            int top  = q.front();
            q.pop();
            flags[top] = true;
            for(auto it : adj[top]) {
                if(!flags[abs(it)]) {
                    if(it > 0) {
                        ans++;
                    }
                    q.push(abs(it));
                }
            }
        }
        return ans;
    }
};