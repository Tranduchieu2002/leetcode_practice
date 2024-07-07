class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        remaining_after_drink = 0
        while (numBottles) >= numExchange:
            remaining_after_drink = (numBottles % numExchange)
            ans += numBottles // numExchange
            numBottles = (numBottles // numExchange) + remaining_after_drink
        
        return ans