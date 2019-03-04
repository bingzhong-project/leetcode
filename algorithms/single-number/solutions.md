# Single Number

[问题描述](https://leetcode.com/problems/single-number/)

## 知识点

位运算

## 解题思路

利用异或运算的特性，有数 num ，一个数与 num 进行异或运算后，将得到的结果再与 num 进行异或运算将会得到 num 。利用该特性，将 num = 0 ，遍历数组，与 0 进行异或运算，如果数字出现过两次，将不会改变 num ，即 num 仍然等于 0 。而如果数字只出现过一次，那么 num 与该数字进行异或运算得到的结果等于数字本身。
