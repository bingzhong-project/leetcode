# Path Sum

[问题描述](https://leetcode.com/problems/path-sum/)

## 知识点

深度优先搜索

## 解题思路

以深度优先搜索得方式遍历树，每次递归到下一个节点前， sum 都减去当前节点的值，作为新的 sum ，当遇到叶子节点且当前 sum 减去节点值等于 0 时，表示有路径和等于 sum 。
