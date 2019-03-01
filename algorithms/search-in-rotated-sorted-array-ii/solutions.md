# Search in Rotated Sorted Array II

[问题描述](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

## 知识点

二分查找

## 解题思路

总体的思路与 [Search in Rotated Sorted Array](https://github.com/bingzhong-project/leetcode/blob/master/algorithms/search-in-rotated-sorted-array/solutions.md) 一样，但是由于数组中存在重复值，所以需要一些特殊的处理。  
数组中存在特殊值，当遇到 nums[mid] == nums[right] 的情况，如 [1,3,1] 和 [1,1,3,1] 。原先的解法将会出错，所以需要处理 nums[mid] == nums[right] 的情况，而处理起来也是很简单，就是 right -= 1 ，将数组的边界缩小。  
其实当 nums[mid] == nums[right] 时，有可能是 mid 与 right 是同一个值，指向同一个元素，这种情况发生，只有 left == right 时，即候选数组中只有一个元素了，而这个元素也不等于 target 时，right -= 1 将会结束查找。  
另一种可能就是 mid 和 right 指向了重复值，这时缩小右边界将不会对结果造成影响，因为还有一个相同的值在候选数组中，不断缩小边界直到 nums[mid] 与 nums[right] 不再相等，之后再次进行查找即可找到目标值。
