# Product of Array Except Self

[问题描述](https://leetcode.com/problems/product-of-array-except-self/)

## 知识点

数组

## 解题思路

位置 i 的乘积，可以通过 0 到 i - 1 的乘积与 i + 1 到 n 的乘积相乘得出，那么分别求出位置 i 的前半部分数组乘积与后半部分数组乘积即可。

其实不需要使用两个数组分别存储，先用要给声明一个数组，位置 i 存储 i + 1 到 n 的乘积。也就位置 i 是后半乘积。而前半部分的乘积不再额外利用数组存储，只利用一个变量去存储即可，在后续遍历数组设置 res 值的时候再逐个计算。
