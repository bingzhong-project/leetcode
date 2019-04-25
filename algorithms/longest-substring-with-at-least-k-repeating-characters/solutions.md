# Longest Substring with At Least K Repeating Characters

[问题描述](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/)

## 知识点

分而治之

## 解题思路

首先对字符串进行字符的统计，然后查看哪些字符出现的次数未够 k 次。未够 k 次的字符肯定不会出现在符合要求的最长子字符串之中，所以以这个字符为切割点，将字符串切割成多个子串，然后子串分别递归重复执行上述过程。  
当得到的一个满足要求的子串时，返回给长度，然后与其他长度结果一起比较，得出最长长度，即为答案。
