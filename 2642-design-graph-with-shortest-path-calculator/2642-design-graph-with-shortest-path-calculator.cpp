class Graph {
    int nodes;
    vector<vector<pair<int,int>>> adj;
public:
    Graph(int n, vector<vector<int>>& edges) {
        nodes = n;
        adj.resize(n);
        for (auto edge : edges) {
            adj[edge[0]].emplace_back(edge[1], edge[2]);
        }
    }
    
    void addEdge(vector<int> edge) {
        adj[edge[0]].emplace_back(edge[1], edge[2]);
    }
    
    int shortestPath(int start, int end) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        vector<int> dist(nodes, INT_MAX);
        pq.push({0, start});
        dist[start] = 0;
        
        while(!pq.empty()) {
            int currentNode = pq.top().second;
            int currentCost = pq.top().first;
            pq.pop();
            
            if (currentCost > dist[currentNode]) {
                continue;
            }
            
            if (currentNode == end) {
                return currentCost;
            }
            
            for (auto edge : adj[currentNode]) { 
                int neiCost = edge.second;
                int nei = edge.first;
                int nextCost = dist[currentNode] + neiCost;
                if (dist[nei] > nextCost) {
                    dist[nei] = nextCost;
                    pq.push({nextCost, nei});
                }
            }
                        
        }
        return dist[end] == INT_MAX ? -1 : dist[end];
        
    }
};

/**
 * Your Graph object will be instantiated and called as such:
 * Graph* obj = new Graph(n, edges);
 * obj->addEdge(edge);
 * int param_2 = obj->shortestPath(node1,node2);
 */