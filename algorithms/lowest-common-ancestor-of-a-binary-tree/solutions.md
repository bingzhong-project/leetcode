# Lowest Common Ancestor of a Binary Tree

[问题描述](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

## 知识点

二叉树

## 解题思路

利用后序遍历从底向上处理结点。若当前结点的左结点或右结点等于 p ，则将 p 更新为当前结点，如果时等于 q ，则将 q 更新为当前结点。这样 p 和 q 会随着遍历不断上升，当 p 和 q 第一次相遇时，即相等时，p 和 q 所指向的就是最近公共父结点。
