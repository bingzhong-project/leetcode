# Valid Sudoku

[问题描述](https://leetcode.com/problems/valid-sudoku/)

## 知识点

哈希表

## 解题思路

遍历给定的二维数组，利用哈希表存储各个数值出现的位置，如 positions[5] = [(0, 0)] ，当遍历时遇到已经存储了位置的数值时，即表示同一个数值出现了一次以上，然后根据 positions 存储的位置判断是否复合数独规定，如果是有效的，就将该位置也存储到 positions 中。
