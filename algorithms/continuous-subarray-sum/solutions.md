# [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)

## 知识点

子数组累加和，数学

## 解题思路

思路为快速求出子数组的累加和，然后进行判断。

另一种思路为在求子数组累加和的基础上利用以下定理：

> 如果 a mod c == b mod c ，那么 (a - b) mod c 等于 0 ，即 (a - b) 为 c 的倍数。

有这种思路后，从 0 开始求子数组的累加和，然后每个子数组的累加和 mod k ，并将结果保存下来，当出现两个相等的结果，即证明有子数组的和为 k 的倍数。

假设 sum[i] 为 0 到第 i 位的子数组累加和，有 sum[2] 和 sum[4] 的 mod k 结果相等，那么有：

sum[4] - sum[2] % k == 0

即子数组 nums[3:5] 的累加和位 k 的倍数。
