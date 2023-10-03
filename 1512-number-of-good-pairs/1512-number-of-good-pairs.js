/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    let ans = 0;
    const cnt = Array(101).fill(0);
    for(const val of nums) {
        ans += cnt[val];
        ++cnt[val];
    }
    return ans;
};