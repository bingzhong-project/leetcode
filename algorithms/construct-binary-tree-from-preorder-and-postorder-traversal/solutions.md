# [Construct Binary Tree from Preorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)

## 知识点

树，树的遍历

## 解题思路

分析树的先序遍历与后序遍历，可以得出以下结论：

1. 在先序遍历 pre 中，以 pre[i] 作为根节点，pre[i + 1] 是其左子节点。
2. 在后序遍历 post 中，以 post[i] 作为根节点，post[i - 1] 是其右子节点。

根据上述的结论，在处理时，总是以 pre[0] 作为根节点，并通过 post 找出其右子节点，以此构建出完整的二叉树。
