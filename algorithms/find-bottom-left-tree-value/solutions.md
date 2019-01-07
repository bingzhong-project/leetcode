# Find Bottom Left Tree Value

[问题描述](https://leetcode.com/problems/find-bottom-left-tree-value/)

## 知识点

深度优先搜索

## 解题思路

通过深度优先搜索遍历树，在遍历的同时记录遍历层数。当遇到叶子节点时，尝试记录叶子节点的值并记录当前层数值为 max_level，只有当前层数大于 max_level 才更新值。
