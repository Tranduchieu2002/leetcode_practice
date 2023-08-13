class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        left, right = 0, 0
        
        ans, cur = 0, 0
        
        mp = {}
        
        if (len(fruits) == 1):
            return 1
        
        while (right < len(fruits)):
            
            if fruits[right] not in mp:
                mp[fruits[right]] = 1
            else:
                mp[fruits[right]] += 1
                
            if len(mp) > 2:
                if  mp[fruits[left]] == 1:
                    mp.pop(fruits[left])
                else:
                    mp[fruits[left]] -= 1
                
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans