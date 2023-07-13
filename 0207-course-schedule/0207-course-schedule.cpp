class Solution {
    vector<bool> visited;
    vector<bool> detect;
public:
    bool canFinish(int n, vector<vector<int>>& p) {
        vector<vector<int>> adj(n);
        detect.resize(n, false);
        visited.resize(n, false);
        for (auto const pairCourses : p) {
            adj[pairCourses[0]].push_back(pairCourses[1]);
        }

        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                if (dfs(i, adj)) return false; // detected cycle
            }
        }
        return true;
    }

    bool dfs(int i, const vector<vector<int>>& adj) {
        visited[i] = true;
        detect[i] = true;

        for (int neighbor : adj[i]) {
            if (!visited[neighbor]) {
                if (dfs(neighbor, adj)) return true;
            }
            else if (detect[neighbor]) {
                return true; // detected cycle
            }
        }

        detect[i] = false; // Reset detect status after visiting all neighbors
        return false;
    }
};
