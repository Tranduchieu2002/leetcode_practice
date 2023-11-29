class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort(reverse = True)
        mine = 0
        i = 0
        while i < len(piles):
            bob = piles.pop()
            
            mine += piles[i + 1]
            i +=2
        
        return mine
            