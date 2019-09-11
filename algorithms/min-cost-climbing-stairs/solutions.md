# [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)

## 知识点

动态规划

## 解题思路

有 dp[i] 为到达第 i 阶梯的最小消费，既有以下状态转移方程：

```python
dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i - 1]
```

由于 dp 中只用到 i - 1 和 i - 2 ，即上一步与上上一步，可以使用两个变量进行优化。
