# Search Insert Position

[问题描述](https://leetcode.com/problems/search-insert-position)

## 知识点

二分查找

## 解题思路

使用二分查找的思路去完成。主要是注意找到插入点的位置。  
假设最后定位到的下标为 i ，那么 target 的插入位置必然是 i 或是 i + 1，取决与它与 nums[i] 的大小。如果 target 小于等于 nums[i] ，那么 target 将插入到数 nums[i] 的前面，那么包括下标 i 在内的元素都会往后移一位，那么 target 的插入下标即为 i 。如果 target 比 nums[i] 大，显而易见的它将会插入到 nums[i] 的后面，即 i + 1 的位置。
