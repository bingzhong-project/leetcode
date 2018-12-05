class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Solution 1
        # if len(prices) == 0:
        #     return 0
        # buy = [0 for _ in range(len(prices))]
        # sell = [0 for _ in range(len(prices))]
        # rest = [0 for _ in range(len(prices))]
        # buy[0] = -prices[0]
        # sell[0] = 0
        # rest[0] = 0
        # for i in range(1, len(prices)):
        #     buy[i] = max(rest[i - 1] - prices[i], buy[i - 1])
        #     sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])
        #     rest[i] = max(rest[i - 1], sell[i - 1])

        # return sell[-1]

        # 优化后的 Solution 2
        # if len(prices) == 0:
        #     return 0
        # buy = [0 for _ in range(len(prices))]
        # sell = [0 for _ in range(len(prices))]
        # buy[0] = -prices[0]
        # sell[0] = 0
        # for i in range(1, len(prices)):
        #     buy[i] = max(sell[i - 2] - prices[i], buy[i - 1])
        #     sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])
        # return sell[-1]

        # 优化后的 Solution 3 ，空间复杂度为 O(1)
        if len(prices) == 0:
            return 0
        buy = -prices[0]
        pre_buy = buy
        sell = 0
        pre_sell = sell
        before_pre_sell = pre_sell
        for i in range(1, len(prices)):
            buy = max(before_pre_sell - prices[i], pre_buy)
            sell = max(pre_buy + prices[i], pre_sell)
            pre_buy = buy
            before_pre_sell = pre_sell
            pre_sell = sell
        return sell
