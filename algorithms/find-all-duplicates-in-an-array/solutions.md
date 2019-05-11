# [Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/)

## 解题思路

整体思路类似于 [Find All Numbers Disappeared in an Array Solution](https://github.com/bingzhong-project/leetcode/blob/master/algorithms/find-all-numbers-disappeared-in-an-array/solutions.md) ，遍历数组并将元素 array[array[i] - 1] 取反，当遇到已经为负数的元素时，说明已经进行过一次处理，即出现了重复，该下标 i 即为重复数。
