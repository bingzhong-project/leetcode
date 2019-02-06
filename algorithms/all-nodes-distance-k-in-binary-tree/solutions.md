# All Nodes Distance K in Binary Tree

[问题描述](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)

## 知识点

深度优先搜索

## 解题思路

题目其实就是求单源路径中，符合指定长度的结点。但是题目给出的是二叉树，所以先要为每个结点标注它们的父结点，只要每个结点都可以指向其父结点，那么树就可以看成是一个“普通”的无向图，然后利用广度优先搜索找出符合路径长度的结点即可。
