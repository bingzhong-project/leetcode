# [Monotone Increasing Digits](https://leetcode.com/problems/monotone-increasing-digits/)

## 知识点

贪心算法

## 解题思路

将数字从高位遍历到低位。将遍历到高位划分为一个组，如果数字符合要求（从高位到低位则数字递减），加入到组中，否则当前遍历到的数的前一位减 1，组中的数字全部变为 9 。
