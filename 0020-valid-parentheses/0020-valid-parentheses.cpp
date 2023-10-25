class Solution {
public:
    bool isValid(string s) {
        if (s.size() == 1) return false;
        unordered_map<char, char> map {
            {'(', ')'},
            {'{', '}'},
            {'[', ']'},
        };
        // st contains open bracket
        stack<char> st;
        for (auto c : s) {
            if (map[c] or st.empty()) {
                st.push(c);
                continue;       
            }
            char closeBracket = c;
            char openBracket = st.top();
            st.pop();
            if (map[openBracket] != closeBracket)
                return false;
        }
        return st.empty();
    }
};