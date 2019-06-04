# [Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/)

## 知识点

动态规划

## 解题思路

对于动态规划题目，首先要分析出状态的变化流程，从而推导出状态转移方程。  
对于该题目，对于给定的字符串数组，每个元素都有选择与不选择两个选项，选择元素，则 m 和 n 减去对应的 0 数量和 1 数量，当前的状态变化为 Y 。而不选择的话，m 和 n 的数量将不变化，当前状态为 N ，接下来就是比较 Y 和 N 状态中，谁的结果较大，使之作为最终选择的最优状态。

参考资料：[Ones and Zeroes Solution](https://leetcode.com/problems/ones-and-zeroes/discuss/261086/Python-EASY-to-understand-with-explanation-beat-98-top-down-and-bottom-up)
