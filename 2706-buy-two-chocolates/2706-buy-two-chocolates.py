class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        n = len(prices)
        choco1, choco2 = prices[0], prices[1]
        if(prices[0] > prices[1]):
            choco1, choco2 = prices[1], prices[0]
        for i in range(2, n):
            if(prices[i] < choco1):
                choco2 = choco1
                choco1 = prices[i]
            elif(prices[i] < choco2):
                choco2 = prices[i]
        
        leftover = money - (choco1 + choco2)
        return leftover if leftover >= 0 else money
            