# Wiggle Subsequence

[问题描述](https://leetcode.com/problems/wiggle-subsequence/)

## 知识点

动态规划

## 解题思路

声明一个数组 dp ，dp[i] 为到达数组第 i 位时最大的摇摆序列长度。当前数组元素为 nums[i] 时，cur_diff = nums[i] - nums[i - 1] ，而 diff = nums[i - 1] - nums[i - 2] ，也就是说 cur_diff 为当前差值，diff 为上一次的差值。有以下状态转移方程：

```python
        dp[i] = dp[i - 1] if cur_diff == 0 else dp[i - 1] + 1  # diff 为空，开始进行遍历处理
dp[i] =
        dp[i - 1] + 1 if (diff < 0 and cur_diff > 0) or (diff > 0 and cur_diff < 0) else dp[i - 1] # diff 不为空
```

之后让 diff = cur_diff ，然后继续遍历。但是这样的话在有相邻相同元素时会发生错误。  
当 diff = cur_diff 前，需要判断 cur_diff ，如果 cur_diff 为 0 时，表示相邻元素相等，这时 diff 保持不变。这样的做法是将相邻相等的元素都视为一个元素来处理。  
最后该数组的最长摇摆序列为 dp[-1] 。
