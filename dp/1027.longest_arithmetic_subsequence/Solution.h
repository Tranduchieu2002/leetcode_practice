//
// Created by michael on 23/06/2023.
//
#include <bits/stdc++.h>

using namespace std;
#ifndef ALGO_SOLUTION_H
#define ALGO_SOLUTION_H


class Solution {
public:
    int longestArithSeqLength(vector<int>& nums) {
        int n = nums.size();
        vector<unordered_map<int, int>> dp(n);
        int maxNum = 2;
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < i; ++j) {
                int diffNum = nums[i] - nums[j];

                if(dp[j].count(diffNum)) {
                    dp[i][diffNum] = dp[j][diffNum] + 1;
                } else {
                    dp[i][diffNum] = 2;
                }

                maxNum = max(maxNum, dp[i][diffNum]);

            }
        }
        return maxNum;
    }
};


#endif //ALGO_SOLUTION_H
