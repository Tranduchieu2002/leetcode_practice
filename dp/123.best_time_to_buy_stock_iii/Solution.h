//
// Created by michael on 23/06/2023.
//
#include <bits/stdc++.h>

using namespace std;
#ifndef ALGO_SOLUTION_H
#define ALGO_SOLUTION_H


class Solution {
    int memo[100001][3][2];
public:
    int maxProfit(vector<int> &prices) {
        memset(memo, -1, sizeof(memo));
        return findMaxProfit(prices, 0, 2, true);
    }

    int findMaxProfit(vector<int> &prices, int i, int limits, bool isBuy) {
        if (i == prices.size()) return 0;
        if (limits == 0) return 0;
        if (memo[i][limits][isBuy] != -1) return memo[i][limits][isBuy];
        int profit;
        if (isBuy) {
            profit = max(-prices[i] + findMaxProfit(prices, i + 1, limits, false),
                         findMaxProfit(prices, i + 1, limits, true));
        } else {
            profit = max(prices[i] + findMaxProfit(prices, i + 1, limits - 1, true),
                         findMaxProfit(prices, i + 1, limits, false));
        }
        return memo[i][limits][isBuy] = profit;
    }
};


#endif //ALGO_SOLUTION_H
