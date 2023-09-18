class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        int n = mat.size();
        int m = mat[0].size();
        priority_queue<pair<int, int>> pq;

        auto search = [](const vector<int>& row) {
            int l = 0;
            int r = row.size() - 1;
            while (l <= r) {
                int mid = (r - l) / 2 + l;
                if (row[mid] == 0) {
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            }
            return l;
        };

        for (int i = 0; i < n; ++i) {
            int soldiers = search(mat[i]);
            pq.push({soldiers, i});

            if (pq.size() > k) {
                pq.pop();
            }
        }

        vector<int> result;
        while (!pq.empty()) {
            result.push_back(pq.top().second);
            pq.pop();
        }
        reverse(result.begin(), result.end());

        return result;
    }
};