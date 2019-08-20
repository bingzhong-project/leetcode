# [Knight Probability in Chessboard](https://leetcode.com/problems/knight-probability-in-chessboard/)

## 知识点

动态规划

## 解题思路

每一步都可以走八个方向，也就是在当前步跳向某个格子的几率为 1 / 8 = 0.125 。如果从开始位置算起，k 步后到达某个格子的几率为 0.125 ^ k 。最后的几率就是可以留在棋盘的格子的几率相加。
