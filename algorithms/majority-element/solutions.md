# Majority Element

[问题描述](https://leetcode.com/problems/majority-element/)

## 知识点

数学，Boyer-Moore 算法

## 解题思路

使用 Boyer-Moore 算法求出数组中的主要数。  
Boyer-Moore 算法的思想为，遍历数组，当遇到一对不相同的数字时，将其删除，最后剩下的就是主要数。  
但是在代码实现上，删除数组元素的操作是耗时的，所以将使用一种计数的方式。具体实现如下：

1. 声明变量 major ，存储主要数，初始值为任意值。声明变量 count ，初始值为 0 ，用于计数。
2. 遍历数组，将数组的元素赋值为 n ，当 count 等于 0 时，major 赋值为 n 。
3. 在遍历过程中，major 等于 n ，表示一个数出现过一次，count 自增一。如果 major 不等于 n ，表示上一个数字与当前数字 n 不同，count 自减一。
4. 完成遍历后，得出的 major 即为主要数。但是当数组中不存在主要数时，最后得出的 major 为数组的第一个元素，所以得出 major 后需要再次遍历数组，计算 major 的出现次数，确认数组存在主要数且 major 为主要数。
