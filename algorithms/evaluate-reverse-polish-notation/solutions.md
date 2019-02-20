# Evaluate Reverse Polish Notation

[问题描述](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

## 知识点

栈

## 解题思路

思路为后缀表达式的处理。遍历给定的字符串数组，当遇到数字时，将数字入栈，而当遇到运算符时，出栈两个数字，进行运算，将运算结果入栈。重复这样的处理直到完成对给定字符串数组的遍历。最后的结果就在栈中，出栈即可。
