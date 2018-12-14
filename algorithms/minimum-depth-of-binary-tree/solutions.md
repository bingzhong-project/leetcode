# Minimum Depth of Binary Tree

[问题描述](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

## 知识点

广度优先搜索

## 解题思路

使用广度优先搜索，注意标记每一层的最后一个节点，然后记录遍历层数，当遇到叶子节点时直接返回层数即可。
