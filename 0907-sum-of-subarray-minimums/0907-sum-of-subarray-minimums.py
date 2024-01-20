mod = 10 ** 9 + 7
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        st = [0]
        dp = [-1] * n
        ans = 0
        for i in range(n):

            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            
            if st:
                j = st[-1]
                dp[i] = dp[j] + arr[i] * (i - j)
            else:
                dp[i] = arr[i] * (i + 1)

            st.append(i)
            ans = (ans + dp[i]) % mod
            
        return ans
        