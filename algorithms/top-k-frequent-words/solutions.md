# [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)

## 知识点

堆

## 解题思路

寻找前 k 个出现次数最多的元素，很明显就是利用堆的特性去完成。  
先对给定的元素进行计数，计数完后入堆，之后再从堆中依次出堆，就得到前 k 个出现次数最多的元素。
