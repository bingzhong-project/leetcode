# Daily Temperatures

[问题描述](https://leetcode.com/problems/daily-temperatures/)

## 知识点

栈

## 解题思路

题目的本质是为数组中的每个数值找到最近一个较大值的距离。这类型题目可以利用栈去解决。  
对给定数组进行遍历，将元素的下标入栈。当当前数值比栈顶元素所指向的数值大时，出栈，并计算距离，重复直到栈为空或者栈顶元素所指向的数值比当前数值大。  
遍历完成后，每个数值都成功找到最近一个较大值的距离。