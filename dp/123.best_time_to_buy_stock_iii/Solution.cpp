//
// Created by michael on 23/06/2023.
//

#include "Solution.h"

int main() {
    vector<int> input = {3,3,5,0,0,3,1,4};

    int expectedAns = 6;

    int ans = Solution().maxProfit(input);

    cout << "Your solution is correct ? " << ans << "   expected : " <<  expectedAns;
    return 0;
}