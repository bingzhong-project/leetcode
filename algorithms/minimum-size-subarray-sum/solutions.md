# Minimum Size Subarray Sum

[问题描述](https://leetcode.com/problems/minimum-size-subarray-sum/)

## 知识点

双指针，二分查找

## 解题思路

题目由两种解题方案，一种为利用双指针，时间复杂度为 O(n) ，一种为利用二分查找，时间复杂度为 O(n㏒n)。

### 双指针

遍历给定数组，指针 i 指向当前遍历到的元素，并对遍历到的元素进行累加，即 sum += nums[i] 。然后还需要一个指针 left ，指向进行累加的子数组的最左边，初始时，指向 0 位元素。而当 sum >= s 时，将 left 指针向右移动，逼近 i 指针，同时 sum - nums[left] ，重复上述行为直到 sum 小于 s 。而结果，最小元素数为 i - left + 1 。

### 二分查找

声明一个数组 sums ，sums[i] 记录 sum(nums[:i]) ，sums[i] = 0 。假设有右边界 right ，有：

```python
sums[right] >= sums[i] + s

```

那么有：

```python
sums[right] - sums[i] >= s

```

那么 right - i 为和大于等于 s 的子数组长度。  

之后需要做得就是找出这个右边界 right 值。这个就是利用二分查找法，不断的逼近最小的 right 。
