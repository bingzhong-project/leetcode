# Insert Delete GetRandom O(1)

[问题描述](https://leetcode.com/problems/insert-delete-getrandom-o1/)

## 知识点

数组，哈希表，设计

## 解题思路

思路为利用一个数组 values 用于存储值，利用一个哈希表 pos 用于存储*值-位置*信息。

插入方法的实现很简单，将值插入到 values 中，然后记录下值-位置信息。

移除方法则是先找出值对应的位置 p ，然后将 values 数组中最后一个值交换到 p ，然后移除最后一位元素即可。最后注意值-位置信息的更新。

随机获取方法利用随机算法获取 values 数组的下标即可。
