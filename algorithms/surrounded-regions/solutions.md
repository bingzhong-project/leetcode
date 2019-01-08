# Surrounded Regions

[问题描述](https://leetcode.com/problems/surrounded-regions/)

## 知识点

深度优先搜索

## 解题思路

解题的思路类似于 [Number of Islands](https://github.com/bingzhong-project/leetcode/blob/master/algorithms/number-of-islands/solutions.md) 。  
根据题目要求，可以从 board 的边界开始查找 O 以此作为开始深度优先搜索的根节点，因为在边界处的 O 不会被变成 X 。利用深度优先搜索遍历找到所有相连的 O ，并将 O 更换为 \$ ，表示遍历过的，不会被变为 X 的 O 元素。  
完成深度优先搜索后，将还是 O 的元素变为 X ，因为这些元素无法通过在边界的 O 元素查找到，即不相通且被 X 元素包围。同时将 \$ 元素复原为 O ，即完成整个处理过程。
