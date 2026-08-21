class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        selling_price = 0
        profit = 0

        for i in range(1,len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            selling_price = prices[i]

            profit = selling_price - min_price

            if max_profit < profit:
                max_profit = profit
        return max_profit