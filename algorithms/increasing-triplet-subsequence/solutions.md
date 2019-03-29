# Increasing Triplet Subsequence

[问题描述](https://leetcode.com/problems/increasing-triplet-subsequence/)

## 解题思路

声明两个变量 left 与 right ，使用这两个变量作为边界值。遍历数组，遇到比 left 小的数，赋值到 left ，当遇到比 left 大而比 right 小时，赋值到 right ，这样 left 始终比 right 小。当遇到一个数比 right 大时，即有 3 个增长的元素。
