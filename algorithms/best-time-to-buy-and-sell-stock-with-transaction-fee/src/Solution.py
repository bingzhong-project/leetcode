class Solution:
    def maxProfit(self, prices: list, fee: int) -> int:
        # buy = [0 for _ in range(len(prices))]
        # sell = [0 for _ in range(len(prices))]
        # buy[0] = -prices[0]
        # for i in range(1, len(prices)):
        #     buy[i] = max(sell[i - 1] - prices[i], buy[i - 1])
        #     sell[i] = max(buy[i - 1] + prices[i] - fee, sell[i - 1])

        # return sell[-1]

        # 解法优化
        pre_buy = -prices[0]
        pre_sell = 0
        buy = 0
        sell = 0
        for i in range(1, len(prices)):
            buy = max(pre_sell - prices[i], pre_buy)
            sell = max(pre_buy + prices[i] - fee, pre_sell)
            pre_buy = buy
            pre_sell = sell

        return sell
