class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [-1 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i and dp[i - coin] != -1:
                    if dp[i] != -1:
                        dp[i] = min(dp[i], dp[i - coin] + 1)
                    else:
                        dp[i] = dp[i - coin] + 1
        return dp[-1]
