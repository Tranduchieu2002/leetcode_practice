//
// Created by michael on 23/06/2023.  1027. Longest Arithmetic Subsequence
//
//Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.
//
//Note that: 1027. Longest Arithmetic Subsequence
//
//A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
//A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).

// Example 1:
//
//Input: nums = [3,6,9,12]
//Output: 4
//Explanation:  The whole array is an arithmetic sequence with steps of length = 3.
//Example 2:
//
//Input: nums = [9,4,7,2,10]
//Output: 3
//Explanation:  The longest arithmetic subsequence is [4,7,10].
#include "Solution.h"


int main() {
    vector<int> input = {3,6,9,12};

    int expectedAns = 4;

    int ans = Solution().longestArithSeqLength(input);

    cout << "Your solution is correct ? " << ans << "   expected : " <<  expectedAns;
    return 0;
}
