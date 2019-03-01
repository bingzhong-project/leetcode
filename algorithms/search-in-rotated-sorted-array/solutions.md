# Search in Rotated Sorted Array

[问题描述](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## 知识点

二分查找

## 解题思路

题目有两种解题思路。

### 思路 1

思路 1 为先利用二分查找找出最小值，而最小值的坐标为偏移位。然后就可以利用这个偏移值将数组看作是一个有序数组一样进行二分查找。

### 思路 2

一个有序数组可以将其分为低区域与高区域，数组从左向右值由低到高。

```text
low -> hight

```

当有序数组旋转后，区域划分如下：

```text
hight -> hight-low -> low

```

hight 区域与 low 区域内还是有序的，从左到右数值大小上升。而 hight-low 表示存在数值从大到小。  
基于上述的区域划分，首先按正常的二分查找开始查找目标值。获取数组中间位置 mid，这时就需要判断中间位置落在了那个区域。如果 nums[mid] < nums[right] 则表示从 mid 开始一直到 right 都是上升的，则 mid 在区域 low 。而如果 nums[mid] > nums[right] 则 mid 在区域 hight 。  
这时根据所在区域再判断 target 与 nums[mid] 的大小，在 low 区中，如果 nums[mid] < target <= nums[right] ，则表示 target 落在了一个顺序增长的区域中，也就是 mid 的右方，否则就是落在了 mid 的左方。  
而在 hight 区中，如果 nums[mid] > target >= nums[left] ，则表示 target 也是落在了一个顺序增长的区域中，这时在 mid 的左方，否则就是落在了 mid 的右方。

本质上来说就是在原二分查找的基础上多了一个值所在区域的判断条件，根据区域的不同，则后续的查找方向也不同。

参考：[Search in Rotated Sorted Array 在旋转有序数组中搜索](http://www.cnblogs.com/grandyang/p/4325648.html)
