# [Degree of an Array](https://leetcode.com/problems/degree-of-an-array/)

## 知识点

数组

## 解题思路

先对给定的数组进行计数，找出出现频率最大的 key ，这个 key 有可能存在多个，所以虽然逐个 key 去计算找出最小的结果。  
假设 key = 2 ，声明 left 和 right 指针，从首尾向数组中部同时开始找值等于 2 的元素，left 和 right 都找到的同时，得到的就是当前 key 的数组长度。利用上述的做法检查所有的 key ，然后得出结果。  
需要注意的是最大频率为 1 的个案，遇到最大频率为 1 的数组，整个算法就会退化成 O(N²) ，但可以知道，当最大频率为 1 时，最小的数组长度肯定为 1 ，优化这种情况即可更好的解决问题。
