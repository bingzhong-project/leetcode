# [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

## 知识点

堆

## 解题思路

这道题是典型的 Top K 问题，构建一个大小固定为 k 的小顶堆，当堆未满，即直接将数值入堆。当堆满后，数值与堆顶元素对比，如果比堆顶元素大，即根据堆的规则进行数值替换。  
这样的话，堆顶元素永远是 Top K 元素。
