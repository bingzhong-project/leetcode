> [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/)

# 知识点
动态规划

# 解题思路
每一天都有三个状态可选择，买，卖以及休息（不买也不卖）。分别为这三种状态建立对应的数组：buy 、sell 、rest ，记录第 i 天对应状态的最大收益。如 buy[i] 为第 i 天选择购买时的最大收益。  
要确定第 i 天各状态的最大收益，需要明确状态转移方程。利用状态机的思想确立各个状态的转移关系，以此来确定状态转移方程。  
![buy-sell-rest 状态机](https://bingzhong-project.gitee.io/public/pictures/buy-sell-rest状态机.png)  

根据状态机，有以下方程：
```
buy[i] = max(rest[i - 1] - prices[i], buy[i - 1])
sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])
rest[i] = max(rest[i - 1], sell[i - 1], buy[i - 1])
```

需要注意的是，不可以出现 buy -> rest -> buy 的情况出现，不过从上面的方程来看，buy[i] 总是小于等于 rest[i] 的，所以 buy -> rest -> buy 总是可以避免出现的，方程也可以进行相应的改写：
```
buy[i] = max(rest[i - 1] - prices[i], buy[i - 1])
sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])
rest[i] = max(rest[i - 1], sell[i - 1])
```

最后的结果为 max(sell[-1], rest[-1]) ，即最后一天要么进行了卖，要么没有进行交易。