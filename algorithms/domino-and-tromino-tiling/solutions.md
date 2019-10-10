# [Domino and Tromino Tiling](https://leetcode.com/problems/domino-and-tromino-tiling/)

## 知识点

动态规划

## 解题思路

参考：[Domino and Tromino Tiling Solution](https://www.cnblogs.com/grandyang/p/9179556.html)

分析骨牌堆叠的规律：

![domino-and-tromino-tiling-picutre](https://bingzhong-project.gitee.io/public/pictures/domino-and-tromino-tiling-picutre.png)

可以得出当 N > 2 时有：

```text
dp[n] = d[n - 1] + dp[n - 2] + 2 * (dp[n - 3] + ... + dp[0])
      = dp[n - 1] + dp[n - 3] + (d[n - 2] + d[n - 3] + 2 * dp(dp[n - 4] + ... + dp[0]))
      = dp[n - 1] + dp[n - 3] + dp[n - 1]
      = 2 * dp[n - 1] + dp[n - 3]
```

然后根据公式进行计算即可。
