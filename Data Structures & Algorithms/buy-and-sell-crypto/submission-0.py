class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        profit = 0

        for sell in range(0, len(prices)):

            if prices[sell] < prices[buy]:
                buy = sell
                
            curr_profit = prices[sell] - prices[buy]
            profit = max(curr_profit, profit)
            
        return profit
            
            





        