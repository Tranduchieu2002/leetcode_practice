class Solution {
public:
    string minWindow(string s, string t) {
        int n = s.size();
        int len = t.size();
        if(n < len) return "";
        unordered_map<char,int> mp;

        int ans = INT_MAX, right = 0, left = 0, start = 0;

        for(int i = 0; i < len;++i) {
            char c = t[i];
            mp[c]++;
        }
        
        while(right < n) {
            char c = s[right];
            if(mp[c] > 0) {
                len --; // skip
            }
            mp[c]--;
            right++;
            while(len == 0) {
                if(right - left < ans) {
                    start = left;
                    ans = right - left;
                }

                mp[s[left]] ++;

                if(mp[s[left]] > 0) len ++;
                
                left++;
            }
        }
        if (ans != INT_MAX)
		    return s.substr(start, ans);
        return "";
        
    }
};