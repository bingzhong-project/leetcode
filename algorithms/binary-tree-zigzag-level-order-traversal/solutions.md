# Binary Tree Zigzag Level Order Traversal

[问题描述](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/)

## 知识点

广度优先搜索，栈

## 解题思路

本题的解题思路有两种，一种为使用广度优先搜索，另外一种为使用栈。

### 解法 1

解法 1 使用广度优先搜索进行求解，在 [Binary Tree Level Order Traversal 解题思路](https://gitee.com/bingzhong-project/leetcode/blob/master/algorithms/binary-tree-level-order-traversal/solutions.md) 的基础上添加一个层数计算，每遇到单层就将缓存起来的节点值结合反转，从而完成题目要求。

### 解法 2

解法 2 使用栈来进行求解。  
从题目中可以分析出，每一层的输出顺序都是相反的，如果每一层节点的入栈顺序相反，出栈时就满足了题目的要求。  
为了达到上面的目的，所以将使用两个栈，两个栈分别存储相邻层的节点。只不过两个栈对入栈的顺序有所不同，一个栈总是先对左节点进行入栈，另一个栈总是对右节点进行入栈，这样当两个栈中的节点分别出栈时，就完成了题目要求的节点输出顺序。
