# Split Array into Fibonacci Sequence

[问题描述](https://leetcode.com/problems/split-array-into-fibonacci-sequence/)

## 知识点

回溯

## 解题思路

回溯的判断条件有三个：

1. 值是否超过了 2 <sup>31</sup>
2. 字符串是否为合法数值
3. 斐波那契数列的限制条件

根据上述的三个条件进行回溯，找出出符合要求的斐波那契数列即可。
