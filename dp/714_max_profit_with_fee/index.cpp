#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int memo[50000][3];
    int maxProfit(vector<int>& prices, int fee) {
        int prevProfit = prices[0];
        int n = prices.size();
        return findMaxProfit(0,true,prices, fee);
    }

    int findMaxProfit(int i, bool isBuy,vector<int> prices, int fee) {

        if(i == prices.size()) return 0;
        if(memo[i][isBuy]) return memo[i][isBuy];
        int maxProfitCanGet = 0;
        if(isBuy) {
            maxProfitCanGet = max(findMaxProfit(i + 1, true, prices, fee), findMaxProfit(i + 1, false, prices, fee) - prices[i]);
        } else {
            maxProfitCanGet = max(findMaxProfit(i + 1, false, prices, fee) , findMaxProfit(i + 1, true, prices, fee) - fee + prices[i]);
        }

        return memo[i][isBuy] = maxProfitCanGet;
    }
};

int main() {
    vector<int> input = {1,3,2,8,4,9};

    cout << Solution().maxProfit(input, 2);
    return 0;
}