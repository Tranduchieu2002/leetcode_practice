class Solution {
public:
    vector<int> relocateMarbles(vector<int>& nums, vector<int>& moveFrom, vector<int>& moveTo) {
     unordered_map<int, int> positions;

        for (int i = 0; i < nums.size(); ++i) {
            positions[nums[i]] = nums[i]; 
        }

        for (int i = 0; i < moveFrom.size(); ++i) {
            int from = moveFrom[i];
            int to = moveTo[i];
            if(from == to) continue;
            if (positions.count(from)) {
                positions[to] = to;
                positions.erase(from);
            }
        }

        vector<int> occupiedPositions;
        for (auto& pair : positions) {
            
            occupiedPositions.push_back(pair.second);
        }

        sort(occupiedPositions.begin(), occupiedPositions.end());
         auto it = unique(occupiedPositions.begin(), occupiedPositions.end());
    
        occupiedPositions.erase(it, occupiedPositions.end());
        return occupiedPositions;
    
    
    }
};