class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                current_profit = price - min_price
                max_profit = max(max_profit, current_profit)
                
        return max_profit