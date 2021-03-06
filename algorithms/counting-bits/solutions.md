# Counting Bits

[问题描述](https://leetcode.com/problems/counting-bits/description/)

## 知识点

动态规划，二进制计算

## 解题思路

假设有数 n ，n \* 2 的二进制位 n 的二进制后加一个 0 。如下：

```text
2 = 10
4 = 100
8 = 100
```

所以数 n 的二进制的 1 的数量等于 n // 2 二进制的 1 的数量，即 res[n] = res[n // 2] 。

而如果数 n 为奇数，那么其二进制的值为 n - 1 的二进制的最后一位 0 变为 1 。如下：

```text
2 = 10
3 = 11

4 = 100
5 = 101

6 = 110
7 = 111
```

所以数 n 的二进制的 1 的数量等于 n - 1 二进制的 1 的数量再加一，即 res[n] = res[n - 1] + 1

即有以下公式：

```text
         res[n] = 0 if n == 0
res[n] = res[n] = res[n // 2] if n % 2 == 0
         res[n] = res[n - 1] + 1 if n % 2 != 0
```

根据上述公式进行编码既可得出结果。
