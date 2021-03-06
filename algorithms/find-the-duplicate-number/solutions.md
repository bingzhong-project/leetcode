# Find the Duplicate Number

[问题描述](https://leetcode.com/problems/find-the-duplicate-number/)

## 知识点

计数，鸽巢原理

## 解题思路

本题可以利用鸽巢原理进行解题。  
给出的数组元素值在区间 [1, n] 中，选取 mid = n / 2 作为比较值，数组元素值小于等于 mid 的元素进入 low 区，而大于 mid 的元素进入 high 区。如果数组中不存在重复值，那么在 low 区元素的个数应该等于 mid ，而 high 区的元素个数应该等于 n - mid ，这种情况为鸽子数量等于巢数量。当数组存在重复值，那么 low 区或是 high 区的元素数量必然变多，使得鸽子数大于巢数。这时哪个区域的鸽子数大于巢数，即重复数在哪个区域。  
根据上面的原理，求出 mid 值，然后找出重复数所在区域，重复上述处理，当区域值只有一个时，重复值即为该区域的值。
