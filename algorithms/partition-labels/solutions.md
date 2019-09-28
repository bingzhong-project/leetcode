# [Partition Labels](https://leetcode.com/problems/partition-labels/)

## 知识点

双指针，贪心算法

## 解题思路

首先声明 counter 对字符进行计数，然后声明左右指针 left 和 right ，right 指针遍历字符串数组，遇到字符 S[right] 则在 counter[S[right]] 减去一，并记录下遇到的字符，当 left 到 right 区间中的字符计数都为 0 时，表明有一个区间符合要求，通过 right - left + 1 求得区间长度，之后 left 赋值为 right + 1 ，开启新的区间。
