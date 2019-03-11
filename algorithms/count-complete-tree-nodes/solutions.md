# Count Complete Tree Nodes

[问题描述](https://leetcode.com/problems/count-complete-tree-nodes/)

## 知识点

满二叉树，完全二叉树，二分查找

## 解题思路

要知道树的结点个数，最简单的方法就是遍历整棵树，计出结点个数，但是题目给出的树为完全二叉树，那就很明显不需要遍历整棵树。  
满二叉树的结点个数为 2^h - 1 ，当满二叉树从右到左缺少若干个叶子节点即为完全二叉树。根据这个特性，可以尝试利用树的高度去计算结点个数，需要遍历的结点树将会少很多。

### 思路 1

思路 1 基于以下思路：满二叉树的结点个数为 2^h - 1 ，而完全二叉树的结点个数为左子树加右子树的结点个数再加一。  
那么做法就是分别计算左子树和右子树的高度，如果两颗树的高度一致，表示树为满二叉树，结点树为 2^h -1 ，如果高度不一致，分别而左子结点和右子结点作为根结点，递归计算结点个数，结点个数为左子树结点数加右子结点数加一。

### 思路 2

思路 2 则是利用了二分查找的思想。以左子结点为基准分别计算左右子树的高度，如果左右子树高度相等，则表示左子树为满二叉树，左子数的结点个数为 2^lh - 1 ，再加上已经被发现的根结点，则目前已知结点数位 2^lh 个。而如果高度不相等，则表示右子树为满二叉树，已知结点数位 2^rh 个。然后再递归的去计算另一边非满二叉树的结点个数，最后即可得到整颗树的结点个数。