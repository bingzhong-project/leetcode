class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prices_num = len(prices)
        max_profit = 0
        if prices_num == 0:
            return max_profit
        i = 0
        buy = prices[0]
        sell = prices[0]
        while i < prices_num - 1:
            while i < prices_num - 1 and prices[i] >= prices[i + 1]:
                i += 1
            buy = prices[i]
            while i < prices_num - 1 and prices[i] <= prices[i + 1]:
                i += 1
            sell = prices[i]
            max_profit += sell - buy
        return max_profit
