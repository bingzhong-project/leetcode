# [Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/)

## 知识点

广度优先搜索

## 解题思路

将问题转换成图，每个基因转变成另一个基因即是结点的连通。而题目求的是变换到目标基因的最少次数，其实就是求单源结点的最短路径，而图是无权的，利用广度优先搜索进行计算求解即可。
