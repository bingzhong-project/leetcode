> [Search Insert Position](https://leetcode.com/problems/search-insert-position)

# 知识点
二分查找

# 解题思路
使用二分查找的思路去完成。  
由于最后想要得到的是一个数的插入点，所以最后应该是得到一个数组下标区间 [n, n + 1] 去判断插入位置。得到区间后，就是比较大小，得到插入位置。