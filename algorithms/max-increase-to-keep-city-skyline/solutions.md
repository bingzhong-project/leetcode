# [Max Increase to Keep City Skyline](https://leetcode.com/problems/max-increase-to-keep-city-skyline/)

## 知识点

数组

## 解题思路

分别找出行列的最大值，每个值都可以增加到 min(row_max, col_max) ，之后计算得到总体的提升值即可。
