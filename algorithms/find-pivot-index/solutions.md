# [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)

## 知识点

数组

## 解题思路

定义 left_sum 为左数组的和，right_sum 为右数组的和，left_sum 初始为 0 ，right_sum 初始为数组的和。  
遍历数组，由于中间索引的指是不计入任何子数组的，所以当索引不为 0 时，left_sum 加上 nums[i - 1]的值，而 right_sum 不论怎么样，都会减去 nums[i] 。
