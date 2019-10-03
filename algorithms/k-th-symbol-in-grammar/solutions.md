# [K-th Symbol in Grammar](https://leetcode.com/problems/k-th-symbol-in-grammar/)

## 知识点

递归

## 解题思路

对于每行的第 K 位的数是有规律可循的。  
对于第 N 行，其前半刚好和 N - 1 相等，后一半则是 N - 1 的取反（0 变 1 ，1 变 0）。  
根据这个规律，设 N - 1 行的长度位 pre_len，如果所寻找的第 N 行第 K 个，K 大于 pre_len ，则第 K 个的值为第 k - pre_len 数的取反。之后进行递归求解即可。
