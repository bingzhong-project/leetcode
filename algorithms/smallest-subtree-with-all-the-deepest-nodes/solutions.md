# [Smallest Subtree with all the Deepest Nodes](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/)

## 知识点

树

## 解题思路

通过深度优先搜索遍历结点，分别求出左右子树的最大深度，如果结点的左右最大深度相等，并且大于等于当前最大深度，即表明该结点的左右子树包含了最深结点，当前结点即为结果。
