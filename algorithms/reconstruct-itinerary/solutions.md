# Reconstruct Itinerary

[问题描述](https://leetcode.com/problems/reconstruct-itinerary/)

## 知识点

图，深度优先搜索，拓扑排序

## 解题思路

题目的本质是对图进行拓扑排序，不过这次是对边的遍历而非顶点的遍历。  
构建邻接矩阵后，利用深度优先搜索遍历图，每次递归处理时，都移除已发现的边，当一个顶点已经没有边时，表示其已经处理完成，加入到结果集。
