class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int i, j, ans = 0;
        int n = s.size();
        vector<int> mp(128, 0);
        i = j = 0;

        while(i < n) {
            mp[s[i]]++;
            while(mp[s[i]] > 1) {
                mp[s[j]]--;
                j++;
            }
            ans = max(i - j + 1, ans);
            ++i;
        }
        return ans;
    }
};