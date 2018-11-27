> [Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset/description/)

# 知识点
动态规划

# 解题思路
首先要了解整除的一个特性，如果 C 能被 B 整除dp[i] 表示第 i 位元素的最长整除子集合的长度。对于第 i 位元素来说，有第 n 位元素（ n < i），nums[i] 能被 nums[n] 整除，那么 dp[i] 就有可能为 dp[n] + 1，如果 dp[n] + 1 大于 dp[i] 的话。
```
dp[i] = max(dp[i], dp[n] + 1) if nums[i] % nums[n] == 0
```

但是题目要求的并不是返回最长的子集长度，而是子集元素，而根据子集元素的收集方式，有以下两种解题思路。

## 思路 1
思路 1 为将数组 dp 直接存储整除子集，那么 len(dp[i]) 为最长整除子集合长度。用一个 max_index 记录最长子集合的元素的索引，最后直接返回 dp[max_index] 即可。  
但是这样的话空间复杂度为 O(n<sup>2</sup>) 。  

## 思路 2
思路 2 的 dp 用于存储最大子集合的长度，而为了能够最长子集合的元素，用一个 subset_indices 数组保存整除子集合的索引序列。用 max_index 记录最长整除子集合的元素索引，之后通过遍历 subset_indices 和利用 max_index 将相关的元素收集起来即可。