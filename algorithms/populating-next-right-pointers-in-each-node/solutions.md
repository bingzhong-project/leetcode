# Populating Next Right Pointers in Each Node

[问题描述](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)

## 知识点

深度优先搜索

## 解题思路

利用深度优先搜索遍历树。由于树是完全二叉树，所以有左子节点必定有右子节点，左子节点的 next 指针直接指向右子节点即可。接下来的问题在于右子节点如何跨子树用 next 指针连接下一个同层节点。这里可以利用之前构建好的 next 指针，通过 next 指针找到同层的子树，然后让右子节点的 next 指针指向相应的节点即可。而如果 next 指针为空，那么表示右子节点为最右节点，其 next 指针指向空。
