class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const auto &a, const auto &b ) {
            return a[1] < b[1];
        });
        int ans = 0, end = -1e5;
        
        for(auto i : intervals) {
            if(i[0] >= end) {
                end = i[1];
            } else ans++;
        }
        return ans;
    }
};