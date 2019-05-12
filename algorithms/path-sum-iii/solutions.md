# [Path Sum III](https://leetcode.com/problems/path-sum-iii/)

## 知识点

树，累加和

## 解题思路

根据问题描述，一种直观的解题方式是遍历树，构建出路径和，然后逐个逐个的检验是否等于目标值。这种解题方法的效率并不高，因为进行了大量冗余的计算。

另外的一种思路为结合求累加和的思路。有一棵退化成链表的树，设为 [1, 2, 3, 4] ，结合题目，就是求出等于目标和的子数组和。  
累加和 sum([2, 3]) 等于 sum([1, 2, 3]) - sum([1]) 。

题目求的是符合累加和的路径数量，设有字典 counts 记录累加和出现次数，初始有 counts[0] = 1 ，因为累加和为 0 总是存在（即数组不进行累加）。假设目标和为 5 ，counts 中有 counts[6 = sum([1, 2, 3])] = 1 和 counts[1 = sums([1])] ，所哟 counts[6 - 5] = 1 ，即表示存在 1 个累加和为 5 的子数组。  
当然，题目给出的并不是数组，而是树，所以需要是对树进行遍历，而在处理路径和时是利用处理数组累加和的形式处理。