class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
         stack<int> st;
         vector<int> ans;
        for(int asteroid : asteroids) {
            bool destroy = false;
            while (!st.empty() && asteroid < 0 && st.top() > 0) {
                int top = st.top();
                if(-asteroid == top) {
                    st.pop();
                    destroy = true;
                    break;
                } 
                if(-asteroid > top) {
                    st.pop();
                } else {
                    destroy = true;
                    break;   
                }
            }
            if(!destroy) st.push(asteroid);
        }
       while (!st.empty()) {
            ans.push_back(st.top());
            st.pop();
        }
        reverse(ans.begin(), ans.end()); // To maintain the correct order
        return ans;
    }
};