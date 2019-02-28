# Minimum Size Subarray Sum

[问题描述](https://leetcode.com/problems/minimum-size-subarray-sum/)

## 知识点

双指针，二分查找

## 解题思路

题目由两种解题方案，一种为利用双指针，时间复杂度为 O(n) ，一种为利用二分查找，时间复杂度为 O(n㏒n)。

### 双指针

遍历给定数组，指针 i 指向当前遍历到的元素，并对遍历到的元素进行累加，即 sum += nums[i] 。然后还需要一个指针 left ，指向进行累加的子数组的最左边，初始时，指向 0 位元素。而当 sum >= s 时，将 left 指针向右移动，逼近 i 指针，同时 sum - nums[left] ，重复上述行为直到 sum 小于 s 。而结果，最小元素数为 i - left + 1 。
