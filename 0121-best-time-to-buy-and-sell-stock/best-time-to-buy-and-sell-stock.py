class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        best_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price

            if profit > best_profit:
                best_profit = profit
        return best_profit
