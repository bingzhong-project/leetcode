# Satisfiability of Equality Equations

[问题描述](https://leetcode.com/problems/satisfiability-of-equality-equations/)

## 知识点

图，深度优先搜索，广度优先搜索

## 解题思路

其实题目的本质为判断无向图的任意两点是否连通。首先根据给出的等式构建邻接矩阵，同时记录下不连通的两个点。构建好邻接矩阵后，就是利用 DFS 或 BFS 去判断给出的点是否连通。
