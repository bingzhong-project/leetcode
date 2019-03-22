# Search a 2D Matrix II

[问题描述](https://leetcode.com/problems/search-a-2d-matrix-ii/)

## 知识点

二分查找

## 解题思路

为矩阵设定上边界，以及左边界，然后分别对行和列进行二分查找，每次完成查找，上边界和左边界都收缩（排除掉已经查找过的行与列），不断重复以上过程，逼近查找到目标元素。
