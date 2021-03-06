# 01 Matrix

[问题描述](https://leetcode.com/problems/01-matrix/)

## 知识点

广度优先搜索

## 解题思路

题目本质上是求出每一个非 0 结点到最近一个 0 结点的距离。而从求距离的角度出发，无疑广度优先搜索是最适合的，从 0 结点开始利用广度优先搜索遍历，求出各个非 0 结点的距 0 最短距离。  
但是从题目看来，我们需要将每个 0 结点作为根结点，然后计算距离。而这样做的话，是会 TLE 的，很明显，这样的做法存在很多冗余的计算。  
而为了解决这个问题，可以利用广度优先搜索层级遍历的特性。将所有 0 结点都视为第一层结点，将其全部入队，而非 0 结点可以将其设置为 INT_MAX ，方便于后续计算处理。  
进行了上述的处理后，根据题目的要求，以上下左右的结点作为子结点，进行广度优先搜索。在处理过程中，将子结点的值更新为当前结点值 + 1 ，即距 0 结点的距离。如果越界了或者当前结点值 + 1 值大于子结点的值，不更新结点的值，因为已经找到了距 0 更短的距离。
