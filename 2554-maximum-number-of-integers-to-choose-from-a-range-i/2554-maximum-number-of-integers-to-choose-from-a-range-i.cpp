class Solution {
public:
    int maxCount(vector<int>& banned, int n, int maxSum) {
        map<int, int> mp;
        for(auto it: banned) {
            mp[it]++;
        }
        int sum = 0, cnt = 0;
        for(int i = 1; i <= n; i++) {
            if(mp[i] == 0 && sum + i <= maxSum) {
                cnt++;
                sum += i;
            }
        }
        return cnt;
    }
};