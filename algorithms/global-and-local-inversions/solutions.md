# [Global and Local Inversions](https://leetcode.com/problems/global-and-local-inversions/)

## 知识点

数组，数学

## 解题思路

问题的思路在于，局部倒置与全局倒置的关系。根据两者的描述，局部倒置一定为全局导致，反之不然，那么问题就可以变为寻找不是局部倒置的全局倒置。  
从尾向前遍历数组，在遍历的时候，维护 A[i::] 中的最小值 m，与 A[i - 2] 比较，如果 m 小于 A[i - 2] ，则表示存在全局倒置不是局部倒置，直接返回 False 。
