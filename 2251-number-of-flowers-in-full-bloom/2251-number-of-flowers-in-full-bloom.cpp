class Solution {
public:
    vector<int> fullBloomFlowers(vector<vector<int>>& flowers, vector<int>& people) {
        vector<int> init_state(people.begin(), people.end());
        sort(people.begin(), people.end());
        sort(flowers.begin(), flowers.end());
        priority_queue<int, vector<int>, greater<int> > pq;
        
        unordered_map<int, int> blooms;
        int cur_flower = 0;
        int n = people.size();
        for (int i = 0; i <  people.size(); ++i) {
            int arrival_time = people[i];
            
            while (cur_flower < flowers.size() and flowers[cur_flower][0] <= arrival_time) 
                pq.push(flowers[cur_flower++][1]);
            
            while (!pq.empty() and pq.top() < arrival_time) 
                pq.pop();
                
            blooms[arrival_time] = (pq.size());
        }
        vector<int> ans;
        for (int i = 0; i < init_state.size(); ++i) {
            ans.push_back(blooms[init_state[i]]);
        }
        return ans;
    }
};