# Range Sum Query - Immutable

[问题描述](https://leetcode.com/problems/range-sum-query-immutable/)

## 知识点

动态规划，数组

## 解题思路

在初始化时预计算出一个数组范围和信息 range 。range[i] 为数组从 0 开始到 i 的和。  
在获取范围和时，如果给定的左边界 left 是 0 ，直接范围 range[right] 即可，否则返回 range[right] - range[left - 1] 。
