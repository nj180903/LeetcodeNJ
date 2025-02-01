
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Initialize min_price to a very high value
        max_profit = 0  # Initialize max_profit to 0

        for price in prices:
            if price < min_price:
                min_price = price  # Update min_price if a lower price is found
            else:
                max_profit = max(max_profit, price - min_price)  # Calculate profit and update max_profit

        return max_profit
