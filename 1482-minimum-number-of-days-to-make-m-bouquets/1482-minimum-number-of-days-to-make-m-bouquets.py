class Solution:
    def minDays(self, bloomDay, m, k):
        def canMakeBouquets(days):
            bouquets = 0
            flowers = 0

            for day in bloomDay:
                if day <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            
            return bouquets >= m

        if m * k > len(bloomDay):
            return -1
        
        left, right = 0, 10**9
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if canMakeBouquets(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans