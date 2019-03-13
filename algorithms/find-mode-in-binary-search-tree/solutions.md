# Find Mode in Binary Search Tree

[问题描述](https://leetcode.com/problems/find-mode-in-binary-search-tree/)

## 知识点

二叉搜索树

## 解题思路

一种很简单的做法为遍历树，将元素以及其出现次数记录下来，然后返回出现次数最多的元素即可。  
而如果不使用额外空间（递归不算），那么可以利用二叉搜索树的排序特性，利用中序遍历可以顺序输出二叉搜索树，如果输出的顺序是顺序的，计算元素的出现次数并找出次数最多的元素是简单的。
