# Smallest String Starting From Leaf

[问题描述](https://leetcode.com/problems/smallest-string-starting-from-leaf/)

## 知识点

二叉树，深度优先搜索

## 解题思路

对给定的二叉树进行后序遍历，自底向上的构建字符串。由于树是二叉树，对于每个结点来说，要不与左子树组建成字符串，要不与右子树组建成字符串，根据这个特性，每次结点选取较小的一边子树组建成字符串即可。
