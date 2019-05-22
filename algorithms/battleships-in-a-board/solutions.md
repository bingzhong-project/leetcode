# [Battleships in a Board](https://leetcode.com/problems/battleships-in-a-board/)

## 解题思路

### 思路 1

思路 1 需要改变数组中的值，通过深度优先搜索发现所有的战舰。

### 思路 2

根据题目分析，可以得出，一艘战舰必然并且仅有一个 X 点的上左位置为空位或是边界，根据这个条件对数组进行遍历，计算出战舰数量。
