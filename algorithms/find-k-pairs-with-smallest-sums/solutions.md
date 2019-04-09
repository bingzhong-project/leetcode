# Find K Pairs with Smallest Sums

[问题描述](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)

## 知识点

堆，排序

## 解题思路

解题的关键主要是利用优先队列和两个数组有序的特性。

先将 (nums1[0], nums2[0]), (nums1[1], nums2[0]), (nums1[2], nums2[0]) ... (nums1[n], nums2[0]) 入队。之后将元素出队，获取到的，肯定就是最小组合。  
元素出队，获取到出队的元素为 (nums1[i], nums2[j]) ，是当前的最小组合。那么下一组可能存在的最小组合在之前入队的元素以及 (nums1[i], nums2[j + 1]) 之中，因为数组都是有序的，这时将 (nums1[i], nums2[j + 1]) 入队。之后重复上述的操作逻辑直到获取到 k 个组合结果。
