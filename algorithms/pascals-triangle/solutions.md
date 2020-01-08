# [Pascal's Triangle](https://leetcode-cn.com/problems/pascals-triangle/)

## 知识点

数组

## 解题思路

二维数组中，每个值 res[i][j] = res[i - 1][j] + res[i - 1][j - 1] ，如果超出边界，当为 0 计算，最后即可得到结果。
