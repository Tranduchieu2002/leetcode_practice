//
// Created by michael on 27/06/2023.
//

#ifndef ALGO_SOLUTION_H
#define ALGO_SOLUTION_H
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        using tp = tuple<int, int, int>;
        int n = nums1.size(), m =  nums2.size();
        priority_queue<tp, vector<tp>, greater<tp>> pq;
        vector<vector<int>> ans;

        // insert 2 smallest element
        pq.push({nums1[0] + nums2[0], 0, 0});

        while(k-- and !pq.empty()) {
            auto [val, i, j] = pq.top();
            cout << i << "   "<< j << endl;
            ans.push_back({nums1[i], nu ms2[j]});
            pq.pop();

            if(j + 1 < m && i < n)
                pq.push({nums1[i] + nums2[j+1], i, j+1});
            if(j < m && i + 1< n && j == 0)
                pq.push({nums1[i + 1] + nums2[j], i + 1, j});
        }
        return ans;
    }
};


#endif //ALGO_SOLUTION_H
