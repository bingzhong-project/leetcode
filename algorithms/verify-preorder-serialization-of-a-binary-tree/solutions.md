# Verify Preorder Serialization of a Binary Tree

[问题描述](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/)

## 知识点

栈

## 解题思路

解题的方式主要是以一种后序遍历的方式去处理，以**左子结点 → 右子节点 → 父结点**的顺序去判断处理结点。当
遍历给定的字符，当遇到非 # 的值时，表示遇到非空结点，往栈中添加元素 element=[False, False] ，表示该结点的左子结点和右子结点还没被发现。  
而遇到 # 值时，表示栈顶元素的左子结点或右子结点为空，将 element 的任一 False 值改为 True ，当 element 中的值都为 True 时，表示栈顶结点的左右结点已被发现，该结点出栈。  
而上述的方式处理，栈中的第 i 个元素总是第 i + 1 个元素的父结点。当栈为空时，表示根结点也被处理完成，如果这时还有结点还未被处理，则表示给定的字符串不是二叉树的前序遍历结果。
