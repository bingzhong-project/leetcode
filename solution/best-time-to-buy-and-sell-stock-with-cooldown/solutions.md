> [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/)

# 知识点
动态规划

# 解题思路
每一天都有三个状态可选择，买，卖以及冷冻期。分别为这三种状态建立对应的数组：buy 、sell 、rest ，记录第 i 天对应状态的最大收益。如 buy[i] 为第 i 天选择购买时的最大收益。  
要确定第 i 天各状态的最大收益，需要明确状态转移方程。利用状态机的思想确立各个状态的转移关系，以此来确定状态转移方程。  
![buy-sell-rest 状态机](https://bingzhong-project.gitee.io/public/pictures/buy-sell-rest状态机.png)  

buy 状态可以从 rest 状态转移，或是不进行购买，延续上一次的购买状态。  
sell 状态可以从 buy 状态转移，或是不进行售出，延续上一次的售出状态。
rest 状态可以从 sell 状态转移，或是延迟上一次的冷冻状态。

根据状态机，有以下方程：
```
buy[i] = max(rest[i - 1] - prices[i], buy[i - 1])
sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])
rest[i] = max(rest[i - 1], sell[i - 1])
```

最后的结果为 max(sell[-1], rest[-1]) ，即最后一天要么进行了卖，要么处于冷冻期。  

而 rest 状态只有进行了 sell 之后才会进入，即每个 rest 状态都是由 sell 状态转移到的。所以由 rest[i] = sell[i - 1] 。  
可以对上述的方程进行优化：
```
buy[i] = max(sell[i - 2] - prices[i], buy[i - 1])
sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])
```

之后可以观察到，其实每次求解对列表中记录的值都只依赖于 i - 1 和 i - 2 ，可以针对这一点进行优化，使空间复杂度为 O(1) 。
```
buy = max(before_pre_sell - prices[i], pre_buy)
sell = max(pre_buy + prices[i], pre_sell)
pre_buy = buy
before_pre_sell = pre_sell
pre_sell = sell
```