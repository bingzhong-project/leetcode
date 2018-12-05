> [Maximal Square](https://leetcode.com/problems/maximal-square/description/)

# 知识点
动态规划，正方形几何

# 解题思路
首先了解一个关于正方形的几何小知识。有下图：  
![正方形组合图](https://bingzhong-project.gitee.io/public/pictures/正方形组合图.png)  

有边长为 2 的正方形，在其右下角添加一个边长为 1 的正方形，将各边连接起来，将会成为边长为 2 + 1 的正方形。  

根据上面的这个小知识，声明一个二维数组 dp ，dp[i][j] 存储的是 matrix[i][j] 作为右下角的正方形边长。  
那么结合题目将有以下公式：
```
           matrix[i][j] if matrix[i][j] == 0 or i == 0 or j == 0
dp[i][j] = 
           min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 # 判断是否可以与周围的边组合成为新的边，如果可以则组成新的正方形，边长 + 1
```

之后通过上述的公式进行编码即可。

参考资料：[Maximal Square Solution](https://leetcode.com/articles/maximal-square/#)