# Lowest Common Ancestor of a Binary Search Tree

[问题描述](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

## 知识点

二叉查找树

## 解题思路

主要是利用二叉查找树的特性，即左子结点比根结点小，右子结点比根结点大。在进行处理时，首先保证 p < q 。如果 p < root 并且 q > root ，即 p 和 q 分别在左子树和右子树中，那么最近公共父母结点为 root 。而如果 p, q < root ，即 p, q 在左子树中，那么以 root.left 作为根结点递归执行。如果 p, q > root ，即 p, q 在右子树中，以 root.right 作为根结点递归执行。
