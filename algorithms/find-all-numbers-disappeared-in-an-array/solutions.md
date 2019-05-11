# [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)

## 解题思路

题目给出的数组元素在 1 ≤ array[i] ≤ len(array) 范围中，遍历数组，将元素 array[array[i] - 1] 取反（已经为负数的元素不再取反）。最后只要再重新遍历一次 array ，找到非负数的元素时，其下标 i 即为消失的数字。
