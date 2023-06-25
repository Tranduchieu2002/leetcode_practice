//
// Created by michael on 25/06/2023.
//

#ifndef ALGO_SOLUTION_H
#define ALGO_SOLUTION_H
#include <bits/stdc++.h>
using namespace std;

class Solution {
    int n;
    vector<vector<int>> memo;
    vector<int> l;
    const int mod = 1e9 + 7;
public:
    int countRoutes(vector<int>& locations, int start, int finish, int fuel) {
        l = locations;
        n = locations.size();

        memo.resize(n, vector<int>(fuel + 1, -1));
        return dp(start, finish, fuel);
    }
    int dp(int cur, int end, int remainFuel) {
        int ans = cur == end;
        if(remainFuel <= 0) return ans;

        if(memo[cur][remainFuel] != -1)
        {
            return memo[cur][remainFuel];
        }

        for(int i = 0; i < n;++i) {
            if(i == cur) continue;
            int rD = (remainFuel - (abs(l[cur] - l[i]) % mod)) % mod;
            if((rD) >= 0) {
                ans  = (ans + dp(i, end, rD)) % mod;
            }
        }
        return memo[cur][remainFuel] = ans % mod;
    }
};


#endif //ALGO_SOLUTION_H
