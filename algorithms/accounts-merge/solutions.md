# [Accounts Merge](https://leetcode.com/problems/accounts-merge/)

## 知识点

深度优先遍历，连通图

## 解题思路

可以将每个邮箱都看程是一个节点，节点之间连通就是可以合并。  
那么做法就是先构建出邻接矩阵，然后利用深度优先遍历找连通节点。
