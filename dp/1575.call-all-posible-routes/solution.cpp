//
// Created by michael on 25/06/2023.
//

#include "solution.h"

int main() {
    Solution *s = new Solution();
    vector<int> input = {2,3,6,8,4};
    cout << s->countRoutes(input, 1, 3, 5);
}

// Input: locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5
