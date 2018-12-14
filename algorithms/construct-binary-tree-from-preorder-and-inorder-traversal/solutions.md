# Construct Binary Tree from Preorder and Inorder Traversal

[问题描述](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)

## 知识点

先序遍历，中序遍历

## 解题思路

首先要了解中序遍历的一个特性，有第 i 尾节点，那么 0..i-1 的节点为其左子树的中序遍历，i+1..n 为其右子树的中序遍历。  
然后再了解先序遍历的特性。先序遍历的节点遍历顺序如下：  
![DFS Preorder](https://bingzhong-project.gitee.io/public/pictures/dfs-preorder.png)

根据先序遍历的遍历顺序，可以总是将先序遍历集合中第一个节点作为根节点，而 1..n 的节点将为该节点的子树的先序遍历集合。但是根据先序遍历的特性，第 i + 1 个节点有可能是第 i 个节点的左子节点，或是右子节点，或非子节点。  
对于上述的三种可能性，需要用到中序遍历的集合来进行判断处理。如果节点的值存在于中序遍历集合中，即表示该节点存在，是某个节点的子节点，否则则为不存在，某个节点的子节点为空。  
根据上面的几个规则特性进行树的构造，则可得到结果。  
资料参考：[Construct Binary Tree From Preorder and Inorder Traversal Solution](https://leetcode.com/articles/construct-binary-tree-from-preorder-and-inorder-tr/#)
