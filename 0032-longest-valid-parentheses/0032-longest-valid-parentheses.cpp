class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> st ({-1});
        int count = 0;
        int ans = 0;
        for (int i = 0; i < s.size(); ++i) {
            char c = s[i];
            if (c == '(') {
                st.push(i);
                continue;       
            }
            st.pop();
            if (st.empty())
                st.push(i);
            else
                ans = max(ans, i - st.top());
        }
        return ans;
    }
};