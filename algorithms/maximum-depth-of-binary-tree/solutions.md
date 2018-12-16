# Maximum Depth of Binary Tree

[问题描述](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

## 知识点

深度优先搜索

## 解题思路

利用深度优先搜索去计算层数，即每一次递归调用，都表示树的层数 +1 。  
做法有以下两种：

1. 递归函数维护一个 level 变量，用于计算层数，当遇到叶子节点时，记录下该 level 。由于树会有多个叶子节点，所以还需要去缓存这些 level 值，并找出最大的值。
2. 第二种方法为分别计算左右子树的深度，每递归一次，层数加一，最后比较左右子树的深度，最大值即为结果。
