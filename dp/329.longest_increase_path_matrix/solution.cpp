//
// Created by michael on 26/06/2023.
//

#include "solution.h"

//Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
//Output: 4
//Explanation: The longest increasing path is [1, 2, 6, 9].
int main() {
    vector<vector<int>> m = {{9,9,4},{6,6,8},{2,1,1}};
    cout << Solution().longestIncreasingPath(m);
}