# [Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/)

## 知识点

动态规划

## 解题思路

先计算出给出字符串的总 ASCII 码总数，然后找出最大 ASCII 码的公共字符串。

定义 dp[i][j] 为字符串 1 第 i 位与字符串第 j 位的最大 ASCII 码公共字符串的 ASCII 码总数。

当 s1[i] == s2[j] ，则最长公共子序列能够增加一位，当前的最大 ASCII 码为：

```text
dp[i][j] = dp[i - 1][j - 1] + ord(s1[i]) + ord(s2[j])
```

若 s1[i] != s2[j] ，则表示当前最长公共子序列没有变化，由于两个字符串需要错位比较，所以当前最大 ASCII 码为：

```text
dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
```
