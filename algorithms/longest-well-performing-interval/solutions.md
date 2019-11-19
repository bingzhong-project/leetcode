# [Longest Well-Performing Interval](https://leetcode.com/problems/longest-well-performing-interval/)

## 知识点

栈，子数组和

## 解题思路

参考：[O(N) Without Hashmap. Generalized Problem&Solution: Find Longest Subarray With Sum >= K.](<https://leetcode.com/problems/longest-well-performing-interval/discuss/335163/O(N)-Without-Hashmap.-Generalized-ProblemandSolution%3A-Find-Longest-Subarray-With-Sum-greater-K>)

根据给出的数组 hours ，把大于 8 的值赋予为 1 ，小于等于 8 的则赋予 -1 ，构建出新的数组 array ，而根据题目要求，其实就是找出 array 中最长的子数组和大于 0 的子数组长度。  
声明一个 array_sum ，存储从 0 到 i 位置的子数组和。有 j > i ，通过 array_sum[j] - array_sum[i] ，即可求出 i 到 j 的子数组和。

有索引 i ，j ，array_sum[i] < array_sum[j] ，如果 array_sum[-1] - array_sum[j] > 0 ，那么 array_sum[-1] - array_sum[i] > 0 也必定大于 0 ，并且子数组长度更大。通过这样的规则，从前往后依此找到索引 i ，array_sum[i] > array_sum[i + n] ，之后从右往左计算 array_sum[j] - array_sum[i] ，判断是否大于 0 ，如果大于 0 ，则符合条件，记录下子数组长度。

这里利用栈找出符合条件的 i ，栈为单调栈，由栈低到栈顶单调递增，存储的是索引 i ，单调递增的是 array_sum[i] ，构建出单调栈后，然后根据上述的步骤，从后往前遍历，如果 array_sum[i] 大于栈顶元素所指向的 array_sum 值，即元素出栈，计算子数组长度。若栈顶的所引致为 n ，那么计算出的子数组长度必然是 n ~ i 的数组的最大符合条件的子数组长度。之后找出所有计算出来得到的子数组长度，找出最大值即可。
