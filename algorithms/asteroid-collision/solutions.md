# Asteroid Collision

[问题描述](https://leetcode.com/problems/asteroid-collision/)

## 知识点

栈

## 解题思路

遍历给定的数组，将数值入栈。当栈不为空，而当前数值为负数，栈顶数值为正数时，即表示会发生碰撞，如果栈顶元素的绝对值小于当前数值的绝对值，进行出栈操作，重复直到栈为空或不会发生碰撞。
