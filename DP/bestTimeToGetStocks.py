class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Assume min is lowest and max = 0
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Check for minimum price
            if price < min_price:
                min_price = price

            # Calculate profit if the product is sold
            profit = price - min_price

            # Gets the new max profit
            if profit > max_profit:
                max_profit = profit
        
        return max_profit