# [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)

## 知识点

栈

## 解题思路

从头遍历字符串，如果字符不是 '#' ，就将字符入栈，如果是 '#' ，则将栈顶元素出栈，最后栈中元素组成的字符串即为最后的结果，之后两者对比即可。
