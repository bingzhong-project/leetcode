# Flatten Nested List Iterator

[问题描述](https://leetcode.com/problems/flatten-nested-list-iterator/)

## 知识点

栈，代码设计

## 解题思路

核心在于平铺数组的平铺方法。  
可以利用栈去存储给定的元素集合。而当栈顶元素为数组时，出栈，然后遍历数组，将元素重新入栈，该方法递归执行，直到栈为空或是栈顶元素为数字。  
平铺方法主要在 hasNext 方法调用时执行。
