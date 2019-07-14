# [Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/)

## 知识点

字符串，动态规划

## 解题思路

该题目的本质在于求两个字符串的最长公共子序列。  
定义 dp[i][j] ，i < len(word1) + 1 ，j < len(word2) + 1 ，表示 word1 前 i 个字符串与 word2 前 j 个字符串的最长公共子序列。  
当 word1[i] == word[j] ，则最长公共子序列又增加了一位，则当前最长公共子序列为：

```text
dp[i][j] = dp[i - 1][j - 1] + 1
```

若 word1[i] != word2[j] ，则表示当前最长公共子序列没有变化，由于两个字符串需要错位比较，所以当前最长公共子序列为：

```text
dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
```

求出最长公共子序列和之后，最后计算出操作数即可。

参考资料：[Delete Operation for Two Strings 两个字符串的删除操作](https://www.cnblogs.com/grandyang/p/7144045.html)
