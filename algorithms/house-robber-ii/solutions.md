# House Robber II

[问题描述](https://leetcode.com/problems/house-robber-ii/description/)

## 知识点

动态规划

## 解题思路

总体的解题思路与 [House Robber 解题思路](https://github.com/bingzhong-project/leetcode/blob/master/algorithms/house-robber/solutions.md) 相同。  
不同的是，本题中给出的数组为环形，即首尾相连。由于首尾相连，所以首尾是互斥的，偷第一间屋子，即不可以偷最后一间屋子，反之亦然。  
转换一下思路，由于首尾互斥，可以假设永远不偷最后一间屋子，求出 1..n-1 的最大收益，记为收益 1 。然后假设永远不偷第一间屋子，求出 2..n 的最大收益，记为收益 2 。  
永远不偷最后一间屋子，即第一间房子可以选择偷或不偷，不受限制，如果选择不偷，其收益最终会包含在收益 2 中，因为收益 2 所表示的是永远不偷第一间屋子达到的最大收益，反之亦然。最后将这两个结果进行比较，较大值者即为结果。
