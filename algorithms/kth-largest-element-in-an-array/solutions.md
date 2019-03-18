# Kth Largest Element in an Array

[问题描述](https://leetcode.com/problems/kth-largest-element-in-an-array/)

## 知识点

堆

## 解题思路

本题是典型的一道优先队列应用题，将数组依次添加到优先队列（数值越大优先度越高）中，然后逐个出队即可。  
很多语言都有现成的优先队列实现，但是使用现成的优先队列的话这题目就没什么难度和意义了，所以自己利用堆构建出优先队列实现。
