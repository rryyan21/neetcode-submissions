class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minBuy = float('inf')
        maxProfit = 0

        for sell in prices:
            minBuy = min(sell,minBuy)

            profit = sell - minBuy
            maxProfit = max(maxProfit, profit)

        if maxProfit < 0:
            return 0 

        return maxProfit