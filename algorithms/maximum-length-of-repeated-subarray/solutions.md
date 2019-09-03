# [Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/)

## 知识点

动态规划

## 解题思路

类似于求最长公共子序列，但是这题要求必须是子数组，即需要是连续的。那么就只有值相等时，才能加一。  
设有 dp[i][j] 为数组 A 的包含第 i - 1 位的子数组与数组 B 的包含第 j - 1 位子数组的最长公共子数组。状态转移方程如下：

```text
            dp[i - 1][j - 1] + 1 if A[i - 1] == B[j - 1]
dp[i][j] =
            0 if A[i - 1] != B[j - 1]
```
