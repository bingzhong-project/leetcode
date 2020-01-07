# [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

## 知识点

二叉树，深度优先搜索

## 解题思路

分别求各个节点的左右子树高度，如果存在节点，它的左右子树高度差大于 1 ，即不是平衡二叉树，否则，即是。
