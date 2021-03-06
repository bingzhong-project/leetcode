# Validate Binary Search Tree

[问题描述](https://leetcode.com/problems/validate-binary-search-tree/description/)

## 知识点

深度优先搜索，二叉查找树

## 解题思路

本题验证的是一颗树是否为一颗二叉查找树，即左子节点小于它的所有上级节点，右子节点大于它的所有上级节点。  
对于二叉查找树的每个节点来说，其值都有一个区间。当然对根节点来说它的区间为 (-∞, +∞) 。假设有节点为 node ，那么它左子节点的范围区间为 (node.parent.min_border, node.val) ，即大于 node 节点的父节点的最小边界，小于 node 节点的值。它的右子节点的范围为 (node.val, node.parent.max_border) ，即大于 node 节点的值，小于 node 父节点的最大边界。  
在递归时分别更新左右子树的边界范围，然后判断节点是否有超过边界范围即可判断出该树是否为正确的二叉查找树。
