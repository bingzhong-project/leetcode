# [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)

## 知识点

数组，双指针

## 解题思路

使用滑动窗口的形式进行值的筛选。窗口内的元素，必须满足累乘小于 k 。  
例如目前的窗口为 [5, 2, 6] ，包含 6 的符合条件的子数组有:

```text
5 2 6
2 6
6
```

根据上述的规则，遍历数组，找出符合条件的窗口，然后计算子数组的个数即可得到答案。
