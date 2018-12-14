# Longest Increasing Subsequence

[问题描述](https://leetcode.com/problems/longest-increasing-subsequence/description/)

## 知识点

动态规划

## 解题思路

声明一个数组 dp ，dp[i] 表示 nums[:i + 1] 子数组的最长的增长数组长度。  
当遍历到第 i 个元素，需要从头开始遍历 nums[:i] 子数组，找出比第 nums[i] 小的元素，设这个比 nums[i] 小的元素，其在 dp 中的值为 length ，那么 nums[:i + 1] 子数组的最长的增长数组长度就有可能为 length + 1 。找出所有比 nums[i] 小的元素 ，通过比较就可以得出 nums[:i + 1] 子数组的最长的增长数组长度。可以得出以下公式：

```
        1 if i == 0
dp[i] =
        max(dp[:i]) + 1 if nums[i] > nums[n] ，n 为 nums[:i]的元素下标
```

最后结果为 max(dp) 。

参考资料：[Longest Increasing Subsequence Solution](https://leetcode.com/problems/longest-increasing-subsequence/solution/#)
