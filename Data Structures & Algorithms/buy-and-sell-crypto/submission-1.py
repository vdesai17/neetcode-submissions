class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Sliding window

        left = 0
        maxProfit = 0

        for right in range(1,len(prices)):

            # calculate profit if prices[right] < prices[left]
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                # prices[left] >= prices[right]
                left = right
        
        return maxProfit
            
            



