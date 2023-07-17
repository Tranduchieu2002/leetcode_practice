class Solution {
public:
vector<int> shortestAlternatingPaths(int n, vector<vector<int>> &redEdges, vector<vector<int>> &blueEdges)
{
    vector<pair<int, int>> adj[n];

    for (auto element : redEdges)
        adj[element[0]].push_back({element[1], 1});

    for (auto element : blueEdges)
        adj[element[0]].push_back({element[1], 2});

    vector<vector<bool>> visited(n, vector<bool>(3, false));
    vector<int> distance(n, -1);
    queue<vector<int>> q;

    q.push({0, 0, 0}); // {node , steps , color }
    visited[0][1] = visited[0][2] = true;
    distance[0] = 0;

    while (!q.empty())
    {
        int node = q.front()[0], steps = q.front()[1], color = q.front()[2];
        q.pop();

        for (auto element : adj[node])
        {
            if (element.second == color)
                continue;
            if (!visited[element.first][element.second])
            {
                visited[element.first][element.second] = true;

                if (distance[element.first] == -1)
                    distance[element.first] = 1 + steps;

                q.push({element.first, 1 + steps, element.second});
            }
        }
    }
    return distance;
}
};