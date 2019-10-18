# [Hand of Straights](https://leetcode.com/problems/hand-of-straights/)

## 知识点

有序列表

## 解题思路

首先是需要判断能够分出长度都为 W 的多个子数组，这个可以用 len(hand) % W 判断。  
对数组元素进行计数，之后遍历数组，每次取出 num - num + W 的数，判断是否存在于数组中，如果不存在，则无法达到题目要求。如果存在，就减少元素的数量。
