> [Perfect Squares](https://leetcode.com/problems/perfect-squares/description/)

# 知识点
动态规划

# 解题思路
声明一个数组 dp ，dp[n] 表示数 n 的完全平方数的最小数目。  
当 n 刚好为完全平方数时，dp[n] 将为 1 。而当 n 不为完全平方数时，dp[n] 可能为 dp[n - i] + dp[i] ，i 为一个小于 n 的完全平方数，而 dp[n - i] + dp[i] 为最小值。所以有以下公式：
```
        1 if n 为完全平方数
dp[n] = 
        min(dp[n - i] + dp[i]) # i 为小于 n 的完全平方数
```

根据上述的公式进行求解，dp 的最后一位即为答案。