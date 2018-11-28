class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        buy = [0 for _ in range(len(prices))]
        sell = [0 for _ in range(len(prices))]
        rest = [0 for _ in range(len(prices))]
        buy[0] = -prices[0]
        sell[0] = 0
        rest[0] = 0
        for i in range(1, len(prices)):
            buy[i] = max(rest[i - 1] - prices[i], buy[i - 1])
            sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])
            rest[i] = max(rest[i - 1], sell[i - 1])

        return max(sell[-1], rest[-1])
