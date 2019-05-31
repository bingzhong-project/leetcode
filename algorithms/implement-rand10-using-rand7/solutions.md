# [Implement Rand10() Using Rand7()](https://leetcode.com/problems/implement-rand10-using-rand7/)

## 知识点

随机算法，拒绝采样

## 解题思路

这道题目的核心在于拒绝采样，拒绝采样就是当随机获取到的结果不符合要求，再次进行随机，直到获取到符合要求的结果。

rand7 无论怎么样组合，必然会产生出不符合要求的结果，所以就需要用到拒绝采样。

详情参考：[Implement Rand10() Using Rand7() Solution](https://leetcode.com/problems/implement-rand10-using-rand7/solution/)
