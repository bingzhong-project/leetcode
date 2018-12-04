class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        buy = 2**31
        for price in prices:
            buy = min(buy, price)
            res = max(res, price - buy)
        return res
