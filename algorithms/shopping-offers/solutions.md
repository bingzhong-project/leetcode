# [Shopping Offers](https://leetcode.com/problems/shopping-offers/)

## 知识点

动态规划

## 解题思路

有多种购买方案，从中找出最优的购买方案，得出最优购买的消费金额。这类题目适用于动态规划进行解答。

如果不购买大礼包，总是可以得出，需要消费的金额为：sum([needs[i] \* price[i] for i in range(len(needs))]) 。  
购买大礼包后，需要购买的物件即 needs 会变为新的状态，如果购买大礼包超过了所需物件数量，即不能购买大礼包。以此为基础，自上而下的构建出解答树，找出每个状态下最小的消费金额，最后即可得出答案。
