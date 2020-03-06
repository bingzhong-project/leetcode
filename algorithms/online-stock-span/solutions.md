# [Online Stock Span](https://leetcode.com/problems/online-stock-span/)

## 知识点

栈

## 解题思路

利用自底向上单调递减的栈存储每一天的价钱和跨度，当不满足单调栈定义时，栈顶元素出栈，新入栈元素的跨度为加上所有出栈元素的跨度。
