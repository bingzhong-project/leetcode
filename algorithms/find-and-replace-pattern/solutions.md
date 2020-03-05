# [Find And Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/)

## 知识点

字符串

## 解题思路

问题需要确定字符串的字符排列是否满足一种指定组合。而本质上，这是需要对字符出现的位置进行判断。  
做法就是判断同一个位置上，word 与 pattern 的同一位置的字符，他们在各自字符串中出现的位置是否一致，如果一致即符合，不然即不符合。
