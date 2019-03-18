# Majority Element II

[问题描述](https://leetcode.com/problems/majority-element-ii/)

## 知识点

数学，众数，Boyer-Moore 算法

## 解题思路

基本思路和 [Majority Element Solution](https://github.com/bingzhong-project/leetcode/blob/master/algorithms/majority-element/solutions.md) 一直。不过不同的是，结果可能是多个元素。但是数组中，出现次数大于 ⌊ n/3 ⌋ 的元素，最多只有两个，这个不多证，稍微想一就明白了。  
接下来还是利用 Boyer-Moore 算法找出结果，不过这次的目标有两个，算法有所改变。最后还需要再次遍历数组，计算得到的两个元素的个数是否大于 ⌊ n/3 ⌋ 。
