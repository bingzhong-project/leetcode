# [Minimum Distance Between BST Nodes](https://leetcode.com/problems/minimum-distance-between-bst-nodes/)

## 知识点

二叉搜索树

## 解题思路

二叉搜索树是有序的，利用中序遍历将节点的值写到数组 arr 中，arr 必然是有序的，对于有序数组来说，最小差必定在 arr[i] - arr[i - 1] 中。之后就是优化掉 arr 数组即可。
