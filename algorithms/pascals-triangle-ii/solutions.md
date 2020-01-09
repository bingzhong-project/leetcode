# [Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/)

## 知识点

杨辉三角，数组

## 解题思路

在杨辉三角二维数组中，每个值 arr[i][j] = arr[i - 1][j] + arr[i - 1][j - 1] ，根据这个性质，在求第 rowIndex 行的数组，随着三角层次递增，不断从后往前遍历，令 res[i] += res[i - 1] 即可。
