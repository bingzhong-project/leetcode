# Kth Smallest Element in a BST

[问题描述](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

## 知识点

二叉查找树

## 解题思路

根据二叉查找树的性质，如果想要将树由小到大的输出，即是对二叉查找树进行中序遍历。按照这个思路，对树进行中序遍历，并计算遍历结点的序号，当序号为 k 时，输出结点的值即可。
