# [Champagne Tower](https://leetcode.com/problems/champagne-tower/)

## 解题思路

参考资料：[Champagne Tower Solution](https://www.cnblogs.com/grandyang/p/9286537.html)

根据给出的题目分析，每个杯最大只能装一瓶酒，多的就往下流。当一个杯满后，向其倒下的酒会分别流下到其临近的两个杯子。  

设有 dp[i][j] ，表示第 i 行第 j 个杯子（i, j 均从 1 开始）经过的酒的数量。  
对于 dp[0][0] ，初始化为所有酒的数量。每个杯都会从其上面临近的杯子得到酒，得到的酒为 1/2 （因为杯子满后从两边流下），而一个杯子装满后才可以流下，所以有

```python
if dp[i][j] >= 1:
    dp[i + 1][j] += (dp[i][j] - 1) / 2
    dp[i + 1][j + 1] += (dp[i][j] - 1) / 2
```
