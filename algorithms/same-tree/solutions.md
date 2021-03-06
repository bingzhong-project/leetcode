# Same Tree

[问题描述](https://leetcode.com/problems/same-tree/)

## 知识点

树，深度优先搜索

## 解题思路

解题思路有两种，都是基于深度优先搜索。

### 思路 1

对树进行遍历，将树的元素节点转化为数组，然后将得到的数组进行比较。空间复杂度为 O(tree1.size + tree2.size) 。

### 思路 2

同样是对树进行遍历，不过这次是同时对两棵树进行遍历。逐个节点逐个节点的比较，当遇到不相等的节点时，返回 False。而如果节点相等，则递归比较下一个子节点，直到两棵树比较完毕。
