//
// Created by michael on 26/06/2023.
//

#ifndef ALGO_SOLUTION_H
#define ALGO_SOLUTION_H
#include <bits/stdc++.h>

using namespace std;

#define ll long long
class Solution {
public:
    long long totalCost(vector<int>& costs, int k, int candidates) {
        ll ans = 0;
        int k1 = k;
        int n = costs.size();
        priority_queue<int, vector<int>, greater<int> > pq;
        priority_queue<int, vector<int>, greater<int> > pq2;
        for(int i = 0; i < candidates; ++i) {
            int headVal = costs[i];
            pq.push(headVal);
        }

        int left = candidates;
        int right = n - candidates -1;
        if(2 * candidates <= n) {
            for(int i = 0; i < candidates; ++i) {
                int tailVal =  costs[n - i - 1];
                pq2.push(tailVal);
            }
        } else {
            for(int i = left; i < n; ++i) {
                int tailVal = costs[i];
                pq2.push(tailVal);
            }
            left = 2;
            right = 1;
        }

        while(k1 > 0) {
            int frontInHead = pq.size()!=0 ? pq.top(): INT_MAX;
            int frontInTail = pq2.size()!=0 ? pq2.top(): INT_MAX;
            cout << right  << "   " << left << endl;
            if(frontInHead <= frontInTail) {
                pq.pop();
                ans += frontInHead;
                if(left <= right) {
                    pq.push(costs[left]);
                    left++;
                }
            } else {
                pq2.pop();
                ans += frontInTail;
                if(left <= right) {
                    pq2.push(costs[right]);
                    right--;
                }
            }
            k1--;
        }
        return ans;
    }
};


#endif //ALGO_SOLUTION_H
