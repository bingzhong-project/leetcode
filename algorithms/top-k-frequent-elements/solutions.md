# Top K Frequent Elements

[问题描述](https://leetcode.com/problems/top-k-frequent-elements/)

## 知识点

堆，哈希表

## 解题思路

先利用哈希表记录下每个数的出现频率，然后构建一个容量大小为 k 的小顶堆，以 (frequent, num) 的方式将元素添加到堆中。之后就是遍历哈希表，遇到当出现频率大于堆顶的元素，将该元素置于堆顶，然后进行堆化，当遍历结束后，堆中的就是出现频率 Top K 的元素。
