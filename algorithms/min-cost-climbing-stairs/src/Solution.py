class Solution:
    def minCostClimbingStairs(self, cost: list) -> int:
        # dp = [0 for _ in range(len(cost) + 1)]
        # dp[1] = cost[0]
        # for i in range(2, len(cost) + 1):
        #     dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i - 1]

        # return min(dp[-1], dp[-2])
        pre_pre = 0
        pre = cost[0]
        for i in range(2, len(cost) + 1):
            cur = min(pre_pre, pre) + cost[i - 1]
            pre_pre = pre
            pre = cur

        return min(pre_pre, pre)
