# [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)

## 知识点

递归

## 解题思路

将数组分成 k 个子集合，且各个子集合的集合和都相等，那么可以得知各个子集合的集合和为 target = sum(nums) // k ，如果 sum(nums) 除不尽 k ，即可直接知道数组无法分出符合条件的集合。

那么接下来的问题就是如何将数组分为 k 个集合，且集合和为 target 。  
由于每个元素都只能用一次，所以需要使用一个 visited 用于标记已经使用的元素。遍历数组，用一个 index 变量记录当前遍历到的下标，并利用一个 cur_sum 变量记录当前的一个子集合和，当子集合和等于 target ，表示找到一个符合条件的子集合，进行递归，并且将 index 和 cur_sum 重置为 0 ，否则一直递归寻找符合条件的集合。  
当 k 等于 1 的时候，表示只需分出一个集合，这时，剩余的元素的和肯定符合条件，因为在开始判断前已经知道了集合是否有可能分出 k 个符合条件的子集合。

参考：[Partition to K Equal Sum Subsets 解题](https://www.cnblogs.com/grandyang/p/7733098.html)
