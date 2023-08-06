class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = {}

        def solve(cur_goal, old_songs):
            if cur_goal == 0 and old_songs == n:
                return 1
            
            if cur_goal == 0 or old_songs > n:
                return 0
            
            if f"{cur_goal}-{old_songs}" in dp: return dp[f"{cur_goal}-{old_songs}"]
            
            ans = ( n - old_songs ) * solve(cur_goal - 1, old_songs + 1)
            
            if old_songs > k:
                ans += (old_songs - k) * solve(cur_goal - 1, old_songs)
            ans = ans % MOD
            
            dp[f"{cur_goal}-{old_songs}"] = ans
            return ans
        ans = solve(goal, 0)
        print(dp)
        return ans