class Solution:
    def change(self, amount: 'int', coins: 'List[int]') -> 'int':
        if len(coins) == 0:
            return 1 if amount == 0 else 0
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]
        for i in range(0, amount + 1, coins[0]):
            dp[0][i] = 1
        for i in range(1, len(coins)):
            for j in range(amount + 1):
                dp[i][j] = dp[i - 1][j] + (dp[i][j - coins[i]]
                                           if j >= coins[i] else 0)
        return dp[-1][-1]
