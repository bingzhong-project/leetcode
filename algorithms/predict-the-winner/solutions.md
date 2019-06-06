# [Predict the Winner](https://leetcode.com/problems/predict-the-winner/)

## 知识点

动态规划，极小化极大算法

## 解题思路

根据题目的描述，可以看出题目为极小化极大的问题，玩家 1 总是使自己获取到的分数最大，而玩家 2 则是总是使玩家 1 获取到的分数最小。然后根据此进行编码，求出玩家 1 可以获取到的最大分数。
